import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import cloudinary
import cloudinary.uploader
import cloudinary.api
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.config["UPLOAD_FOLDER"] = "static/uploads"


cloudinary.config(cloud_name=os.getenv("CLOUD_NAME"),
                api_key=os.getenv("API_KEY"),
                api_secret=os.getenv("API_SECRET"))


mongo = PyMongo(app)
ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg", "gif"]


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #check if username already exists in db
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


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #check if username exists in db
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
                #invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # find current user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


@app.route("/get_listings")
def get_listings():
    listings = mongo.db.listings.find()
    return render_template("listings.html", listings=listings)


@app.route("/display_listing/<listing_id>")
def display_listing(listing_id):
    listing = mongo.db.listings.find_one({"_id": ObjectId(listing_id)})
    return render_template("listing.html", listing=listing)


@app.route("/add_listing", methods=["GET", "POST"])
def add_listing():
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
            "created_by": session["user"]
        }
        mongo.db.listings.insert_one(listing)
        flash("Listing Added")
        return redirect(url_for("get_listings"))
    return render_template("add_listing.html")


@app.route("/edit_listing/<listing_id>", methods=["GET", "POST"])
def edit_listing(listing_id):
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
    listing = mongo.db.listings.find_one({"_id": ObjectId(listing_id)})
    return render_template("edit_listing.html", listing=listing)


@app.route("/delete_listing/<listing_id>")
def delete_listing(listing_id):
    mongo.db.listings.delete_one({"_id": ObjectId(listing_id)})
    flash("Listing Deleted")
    return redirect(url_for("get_listings"))


@app.route("/get_features")
def get_features():
    features = list(mongo.db.features.find().sort("feature_name", 1))
    return render_template("features.html", features=features)


@app.route("/add_feature")
def add_feature():
    return render_template("add_feature.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),
            debug=True)