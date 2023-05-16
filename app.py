# imports dependencies
import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from functools import wraps
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import cloudinary
import cloudinary.uploader
import cloudinary.api
if os.path.exists("env.py"):
    import env


# creates an instance of Flask named app
app = Flask(__name__)


# fetches hidden env variables
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.config["UPLOAD_FOLDER"] = "static/uploads"


# fetches cloudinary env variables
cloudinary.config(cloud_name=os.getenv("CLOUD_NAME"),
                api_key=os.getenv("API_KEY"),
                api_secret=os.getenv("API_SECRET"))


# assigns pymongo app to variable mongo
mongo = PyMongo(app)


# sets extensions allowed for images uploaded to cloudinary
ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg", "gif"]


# WRAPPERS
# LOGIN REQUIRED WRAPPER
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            flash("Please login to view this page")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# SUPERUSER REQUIRED WRAPPER
def superuser_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        is_superuser = mongo.db.users.find_one(
        {"username": session["user"]})["is_superuser"]
        if is_superuser == "off":
            flash("You must be a superuser to view this page")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# ROUTES

# HOME VIEW
@app.route("/")
def home():
    """
    renders home page
    """
    return render_template("home.html")


# BUY VIEW
@app.route("/buy")
def buy():
    """
    renders buy page
    """
    return render_template("buy.html")


# REGISTER VIEW
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    render register page
    check if username already registered
    allow new user to register
    enter user into mongodb database
    redirect to profile page

    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# LOGIN VIEW
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    render login page
    check if username already registered
    ensure hashed password matches user input
    redirect to profile page if login successful
    redirect to login page if username or password unsuccessful

    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(
                    url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# LOGOUT VIEW
@app.route("/logout")
def logout():
    """
    remove user from session cookies
    redirect to login page

    """
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# PROFILE VIEW
@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    """
    find current user's username from the db
    render profile page
    pass through username for welcome message

    """
    # find current user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    return render_template("profile.html", username=username)


# DISPLAY USERS VIEW
@app.route("/get_users/<username>", methods=["GET", "POST"])
@login_required
@superuser_required
def get_users(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    users = list(mongo.db.users.find())
    return render_template("users.html", username=username, users=users) 


# EDIT USER VIEW
@app.route("/edit_user/<user_id>", methods=["GET", "POST"])
@login_required
@superuser_required
def edit_user(user_id):
    if request.method == "POST":
        is_superuser = "on" if request.form.get("is_superuser") else "off"
        apply = {
            "is_superuser": is_superuser
        }
        mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": apply})
        flash("User Update Applied")
        return redirect(url_for("get_users", username=session['user'], user_id=session['user']))
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("edit_user.html", user=user)


# DELETE USER VIEW
@app.route("/delete_user/<user_id>")
@login_required
@superuser_required
def delete_user(user_id):
    """
    delete requested user
    redirect to get_users view

    """
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    flash("User Deleted")
    return redirect(url_for("get_users", username=session['user'], user_id=session['user']))


# DASHBOARD / USER'S LISTINGS VIEW
@app.route("/dashboard/<username>", methods=["GET", "POST"])
@login_required
def dashboard(username):
    """
    find current user's username from the db
    render dashboard page
    pass through username for welcome message

    """
    # find current user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    listings = mongo.db.listings.find()
    return render_template(
        "dashboard.html", username=username, listings=listings)


# CARAVAN DETAILS VIEW
@app.route("/caravan_details/<username>", methods=["GET", "POST"])
@login_required
@superuser_required
def caravan_details(username):
    """
    find current user's username from the db
    render profile page
    pass through username for welcome message

    """
    # find current user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    makes = mongo.db.caravan_makes.find()
    models = mongo.db.caravan_models.find().sort("caravan_model", 1)
    features = mongo.db.features.find()
    locations = mongo.db.locations.find()
    return render_template(
        "caravan_details.html", username=username, makes=makes, 
        models=models, features=features, locations=locations)


# DISPLAY ALL LISTINGS VIEW
@app.route("/get_listings")
def get_listings():
    """
    find all the listings in the db
    render profile page

    """
    listings = mongo.db.listings.find()
    return render_template("listings.html", listings=listings)


# DISPLAY ONE LISTNG VIEW
@app.route("/display_listing/<listing_id>")
def display_listing(listing_id):
    """
    find listing requested
    render listing page with requested listing

    """
    listing = mongo.db.listings.find_one({"_id": ObjectId(listing_id)})
    return render_template("listing.html", listing=listing)


# ADD LISTING VIEW
@app.route("/add_listing", methods=["GET", "POST"])
@login_required
def add_listing():
    """
    render add listing page
    upload image to cloudinary
    add listing document to listings db
    redirect to listings page

    """
    if request.method == "POST":
        image_to_upload = request.files["image"]
        if image_to_upload:
            image_upload = cloudinary.uploader.upload(
                image_to_upload, upload_preset="ulau1prq")
        listing = {
            "make": request.form.get("make"),
            "model": request.form.get("model"),
            "length": request.form.get("length"),
            "width": request.form.get("width"),
            "price": request.form.get("price"),
            "beds": request.form.get("beds"),
            "sleeps": request.form.get("sleeps"),
            "location": request.form.get("location"),
            "description": request.form.get("description"),
            "image": image_upload["secure_url"],
            "created_by": session["user"],
            "features": request.form.getlist("features")
        }
        mongo.db.listings.insert_one(listing)
        flash("Listing Added")
        return redirect(url_for("get_listings"))
    features = mongo.db.features.find().sort("feature_name", 1)
    makes = mongo.db.caravan_makes.find().sort("caravan_make", 1)
    models = mongo.db.caravan_models.find().sort("caravan_model", 1)
    locations = mongo.db.locations.find().sort("location", 1)
    return render_template(
        "add_listing.html", features=features, makes=makes, models=models, 
        locations=locations)


# EDIT LISTING VIEW
@app.route("/edit_listing/<listing_id>", methods=["GET", "POST"])
@login_required
def edit_listing(listing_id):
    """
    render edit listing page with current listing info
    upload new image to cloudinary
    replace document info as required
    redirect to listings page

    """
    if request.method == "POST":
        image_to_upload = request.files["image"]
        if image_to_upload:
            image_upload = cloudinary.uploader.upload(
                image_to_upload, upload_preset="ulau1prq")
        submit = {
            "make": request.form.get("make"),
            "model": request.form.get("model"),
            "length": request.form.get("length"),
            "width": request.form.get("width"),
            "price": request.form.get("price"),
            "beds": request.form.get("beds"),
            "sleeps": request.form.get("sleeps"),
            "location": request.form.get("location"),
            "description": request.form.get("description"),
            "image": image_upload["secure_url"],
            "created_by": session["user"]
        }
        mongo.db.listings.update_one({"_id": ObjectId(listing_id)}, {"$set": submit})
        flash("Listing Updated")
        return redirect(url_for("get_listings"))
    features = mongo.db.features.find().sort("feature_name", 1)
    makes = mongo.db.caravan_makes.find().sort("caravan_make", 1)
    models = mongo.db.caravan_models.find().sort("caravan_model", 1)
    locations = mongo.db.locations.find().sort("location", 1)
    listing = mongo.db.listings.find_one({"_id": ObjectId(listing_id)})
    return render_template(
        "edit_listing.html", features=features, makes=makes, 
        models=models, locations=locations, listing=listing)


# DELETE LISTING VIEW
@app.route("/delete_listing/<listing_id>")
@login_required
def delete_listing(listing_id):
    """
    delete requested listing
    redirect to listings page

    """
    mongo.db.listings.delete_one({"_id": ObjectId(listing_id)})
    flash("Listing Deleted")
    return redirect(url_for("get_listings"))


# ADD FEATURE VIEW
@app.route("/add_feature", methods=["GET", "POST"])
@login_required
@superuser_required
def add_feature():
    """
    render add feature page
    add feature document to features db
    redirect to features page

    """
    if request.method == "POST":
        # check if caravan  feature already exists in db
        existing_feature = mongo.db.features.find_one(
            {"feature_name": request.form.get("feature_name")})

        if existing_feature:
            flash("Feature already exists")
            return redirect(url_for("caravan_details", username=session['user']))

        feature = {
            "feature_name": request.form.get("feature_name").lower()
        }
        mongo.db.features.insert_one(feature)
        flash("New Feature Added")
        return redirect(url_for("caravan_details", username=session['user']))
    return render_template("add_feature.html")


# EDIT FEATURE VIEW
@app.route("/edit_feature/<feature_id>", methods=["GET", "POST"])
@login_required
@superuser_required
def edit_feature(feature_id):
    """
    render edit feature page with current feature info
    replace document info as required
    redirect to features page

    """
    if request.method == "POST":
        submit = {
            "feature_name": request.form.get("feature_name").lower()
        }
        mongo.db.features.update_one(
            {"_id": ObjectId(feature_id)}, {"$set": submit})
        flash("Feature Updated")
        return redirect(url_for("caravan_details", username=session['user']))
    feature = mongo.db.features.find_one({"_id": ObjectId(feature_id)})
    return render_template("edit_feature.html", feature=feature)


# DELETE FEATURE VIEW
@app.route("/delete_feature/<feature_id>")
@login_required
@superuser_required
def delete_feature(feature_id):
    """
    delete requested feature
    redirect to features page

    """
    mongo.db.features.delete_one({"_id": ObjectId(feature_id)})
    flash("Feature Deleted")
    return redirect(url_for("caravan_details", username=session['user']))

# ADD MAKE VIEW
@app.route("/add_make", methods=["GET", "POST"])
@login_required
@superuser_required
def add_make():
    """
    render add caravan make page
    add new caravan make to db
    redirect to caravan details page

    """
    if request.method == "POST":
        # check if caravan  make already exists in db
        existing_make = mongo.db.caravan_makes.find_one(
            {"caravan_make": request.form.get("caravan_make")})

        if existing_make:
            flash("Make already exists")
            return redirect(url_for("caravan_details", username=session['user']))

        make = {
            "caravan_make": request.form.get("caravan_make").lower()
        }
        mongo.db.caravan_makes.insert_one(make)
        flash("New Caravan Make Added")
        return redirect(url_for("caravan_details", username=session['user']))
    return render_template("add_caravan_make.html")


# EDIT MAKE VIEW
@app.route("/edit_make/<make_id>", methods=["GET", "POST"])
@login_required
@superuser_required
def edit_make(make_id):
    """
    render edit caravan make page with current make info
    replace document info as required
    redirect to caravan details page

    """
    if request.method == "POST":
        # check if caravan  make already exists in db
        existing_make = mongo.db.caravan_makes.find_one(
            {"caravan_make": request.form.get("caravan_make")})

        if existing_make:
            flash("Make already exists")
            return redirect(url_for("caravan_details", username=session['user']))

        submit = {
            "caravan_make": request.form.get("caravan_make").lower()
        }
        mongo.db.caravan_makes.update_one(
            {"_id": ObjectId(make_id)}, {"$set": submit})
        flash("Caravan Make Updated")
        return redirect(url_for("caravan_details", username=session['user']))
    make = mongo.db.caravan_makes.find_one({"_id": ObjectId(make_id)})
    return render_template("edit_caravan_make.html", make=make)


# DELETE MAKE VIEW
@app.route("/delete_make/<make_id>")
@login_required
@superuser_required
def delete_make(make_id):
    """
    delete requested caravan make
    redirect to caravan details page

    """
    mongo.db.caravan_makes.delete_one({"_id": ObjectId(make_id)})
    flash("Caravan Make Deleted")
    return redirect(url_for("caravan_details", username=session['user']))


# ADD MODEL VIEW
@app.route("/add_model", methods=["GET", "POST"])
@login_required
@superuser_required
def add_model():
    """
    render add caravan model page
    add new caravan model to db
    redirect to caravan details page

    """
    if request.method == "POST":
        # check if caravan  model already exists in db
        existing_model = mongo.db.caravan_models.find_one(
            {"caravan_model": request.form.get("caravan_model")})

        if existing_model:
            flash("Model already exists")
            return redirect(url_for("caravan_details", username=session['user']))
            
        model = {
            "caravan_model": request.form.get("caravan_model").lower()
        }
        mongo.db.caravan_models.insert_one(model)
        flash("New Caravan Model Added")
        return redirect(url_for("caravan_details", username=session['user']))
    return render_template("add_caravan_model.html")


# EDIT MODEL VIEW
@app.route("/edit_model/<model_id>", methods=["GET", "POST"])
@login_required
@superuser_required
def edit_model(model_id):
    """
    render edit caravan model page with current model info
    replace document info as required
    redirect to caravan details page

    """
    if request.method == "POST":
        # check if caravan  model already exists in db
        existing_model = mongo.db.caravan_models.find_one(
            {"caravan_model": request.form.get("caravan_model")})

        if existing_model:
            flash("Model already exists")
            return redirect(url_for("caravan_details", username=session['user']))

        submit = {
            "caravan_model": request.form.get("caravan_model").lower()
        }
        mongo.db.caravan_models.update_one(
            {"_id": ObjectId(model_id)}, {"$set": submit})
        flash("Caravan Model Updated")
        return redirect(url_for("caravan_details", username=session['user']))
    model = mongo.db.caravan_models.find_one({"_id": ObjectId(model_id)})
    return render_template("edit_caravan_model.html", model=model)


# DELETE MODEL VIEW
@app.route("/delete_model/<model_id>")
@login_required
@superuser_required
def delete_model(model_id):
    """
    delete requested caravan model
    redirect to caravan details page

    """
    mongo.db.caravan_models.delete_one({"_id": ObjectId(model_id)})
    flash("Caravan Model Deleted")
    return redirect(url_for("caravan_details", username=session['user']))


# ADD LOCATION VIEW
@app.route("/add_location", methods=["GET", "POST"])
@login_required
@superuser_required
def add_location():
    """
    render add location page
    add new location to db
    redirect to caravan details page

    """
    if request.method == "POST":
        # check if location already exists in db
        existing_location = mongo.db.locations.find_one(
            {"location": request.form.get("location")})

        if existing_location:
            flash("Location already exists")
            return redirect(url_for("caravan_details", username=session['user']))
           
        location = {
            "location": request.form.get("location").lower()
        }
        mongo.db.locations.insert_one(location)
        flash("New Location Added")
        return redirect(url_for("caravan_details", username=session['user']))
    return render_template("add_location.html")


# EDIT LOCATION VIEW
@app.route("/edit_location/<location_id>", methods=["GET", "POST"])
@login_required
@superuser_required
def edit_location(location_id):
    """
    render edit location page with current location info
    replace document info as required
    redirect to caravan details page

    """
    if request.method == "POST":
        # check if location already exists in db
        existing_location = mongo.db.locations.find_one(
            {"location": request.form.get("location")})

        if existing_location:
            flash("Location already exists")
            return redirect(url_for(
                "caravan_details", username=session['user']))

        submit = {
            "location": request.form.get("location").lower()
        }
        mongo.db.locations.update_one(
            {"_id": ObjectId(location_id)}, {"$set": submit})
        flash("Location Updated")
        return redirect(url_for("caravan_details", username=session['user']))
    location = mongo.db.locations.find_one({"_id": ObjectId(location_id)})
    return render_template("edit_location.html", location=location)


# DELETE LOCATION VIEW
@app.route("/delete_location/<location_id>")
@login_required
@superuser_required
def delete_location(location_id):
    """
    delete requested location
    redirect to caravan details page

    """
    mongo.db.locations.delete_one({"_id": ObjectId(location_id)})
    flash("Location Deleted")
    return redirect(url_for("caravan_details", username=session['user']))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),
            debug=True)