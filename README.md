# Caravansy

![Image showing the Caravansy website on various devices](/static/readme-images/testing/responsive-home-screen.webp "Caravansy")

View the deployed site: [Caravansy](https://caravansy-project.herokuapp.com/)

This is Caravansy, a CRUD-based website for users to buy and sell static caravans. The website will enable users to add and manage their static caravan listings and for other users to browse and search available static caravans and contact their owners.

The purpose of this website is to draw, push, manipulate and store data.

Python, Javascript, HTML and CSS will be the languages used to create this website.

# Table of Contents

- [`User Experience`](#user-experience)
    - [`Project Goals`](#project-goals)
    - [`User Experience`](#user-experience)
    - [`User Stories`](#user-stories)
- [`Design`](#design)
    - [`Database Schema`](#database-schema)
    - [`Wireframes`](#wireframes)
    - [`Colour`](#colour)
    - [`Typography`](#typography)
    - [`Code Structure`](#code-structure)
    - [`Structure`](#structure)
    - [`Defensive Design`](#defensive-design)
- [`Features`](#features)
    - [`Unrestricted Areas`](#unrestricted-areas)
    - [`User Area`](#user-area)
    - [`Super User Area`](#super-user-area)
    - [`Error Handlers`](#error-handlers)
- [`Technologies Used`](#technologies-used)
    - [`Languages`](#languages)
    - [`Framework`](#framework)
    - [`Database`](#database)
    - [`Tools`](#tools)
- [`Bugs`](#bugs)
    - [`Fixed Bugs`](#fixed-bugs)
    - [`Known Bugs`](#known-bugs)
- [`Testing`](#testing)
- [`Wishlist`](#wishlist)
- [`Deployment`](#deployment)
- [`Credits`](#credits)

# USER EXPERIENCE (UX)

## Project Goals

### User Goals:

As a seller, I want to:

- access a user-friendly, easily navigable and intuitive website
- list my static caravans for sale
- add individual details about my caravan
- edit individual details about my caravans
- delete caravans I have for sale
- receive messages from users interested in my listings
- the ability to contact the site owner

As a buyer, I want to:

- be able to view all static caravans available
- view details of each individual static caravan
- search for certain charateristics I want in a caravan
- contact the seller for more information

### Site Owner Goals:

- allow users to browse and search all available static caravans
- allow users to register and list caravans they have for sale
- ensure quality listings - through management of specific caravan details
- add and manage my own caravan listings
- manage users - by adding them or removing them as superusers

## User Experience
### Target Audience
* Static caravan private sellers
* Static caravan trade sellers
* Static caravan buyers

### User Requirements and Expectations
* A simple and intuitive navigation system
* An easy way to browse listings
* A clear way to see details of each listing
* Good presentation and a visually appealing design regardless of screen size
* An easy way to contact the listing owner
* Accessible for all users

## User Stories
### User
As a user, I want to:

1. Browse caravan listings
2. Know how to get in touch with the owner
3. Be able to register
4. Be able to list a caravan to sell
5. View my listings
6. Change my details

### Site Owner
As a site owner I want:
1. users to achieve the user stories listed above
2. to be able to turn certain users into superusers
3. add, edit and delete certain caravan details

# DESIGN

## Database Schema
After working through the user stories and thinking through how the database might work, MongoDB was chosen as the intended database. This is because there were not many relationships between all the tables, mainly each table had one relationship to the listing table. Also, going forward, the flexibility that a non-relational database has fits well with this sites purpose. It will allow messaging in the future between owner and buyer.

The database schema was purposefully kept simple and clean for maintainability and scability reasons. 

![Schema](/static/readme-images/general/database-schema.webp "Schema")

## Wireframes

The design was to keep the interface as simple and clear as possible. Design conventions were adhered to for ease of use. 

The following wireframes were created near the beginning of the design process with [Balsamiq](https://balsamiq.com/wireframes/?gclid=CjwKCAiAhKycBhAQEiwAgf19etPR1ccdA0Aiezm63MsBy4PezCLSlN1T14ubQH1pMB7oa7Hz9YqWHhoC-VEQAvD_BwE).

![Wireframes](/static/readme-images/wireframes/wireframes.webp "Caravansy wireframes")

## Colour
The colour palette was design to be clear and simple, with the ability to highlight important pieces of information. 

* Green #2bfc82
* White #fff
* Black #000

![The colour palette chosen for the website](/static/readme-images/general/color-palette.webp "Colour Palette")

## Typography

[Google Fonts](https://fonts.google.com/) was used to obtain fonts used.

The Open Sans font is the font used throughout the site, in different weights and font-sizes. This keeps the simplicity of the site in focus. It is used frequently by many web developers and is easy on the eye. Sans Serif is set as a backup should the Poppins font fail to load.

## Code Structure
Bootstrap grid system and responsiveness were used throughout the site and the HTML was organised in an effective way according to bootstrap useability. 

The CSS file was written in a way to utilise the cascading nature of CSS and in such a manner that general styles including colors are found at the top, then styles for each section as found in their defined order (as found when browsing the site) and then media queries at the bottom.

Javascript was utilised to for simple interactivity. For example, displaying the phone number and email address of the listing owner.

## Structure
The site is structured in a familiar, user friendly way. A familiar navigation menu is included in the layout . The menu is hidden using a hamburger menu icon as a toggle on smaller devices. 

A second navigation menu is found in the dashboard once logged in. It's displayed a sidebar.

## Defensive Design
To prevent user error and instruct users in the case of an error, defensive design strategies were used:
- error handler routes were created to deal with the most common errors. A single error page was design. The different error handles redirect the user to that same page and pass through the relevant message.
- validation of forms was done by using the required attribute, using regex patterns, min and max length and types.
- it a user tries to delete something, a modal pops up informing the user that this action cannot be undone and they must press another button to complete the delete action.
- Certain parts of the website can only be access by a logged in user and further to this certain part of the website can only be accessed by superusers. Wrappers were used to decorate routes that required these and this prevented reguritating code for each route.

# FEATURES

## Unrestricted Areas

### Home Page

![Home Page](/static/readme-images/pages/home-page-screenshot.webp "Home Page")

The home page is a simple introduction to the website helping users to understand what the company does. It has effective imagery and link buttons to help users navigate to their chosen area easily. If the user is already logged in, the link text and redirect route changes. For example, if the user is not logged in, the 'List Caravan' button redirects the user to the register page (which has text saying you must register to add a listing). If the user is logged in, the button redirects the user to the add listing page.

### Buy Page

![Buy Page](/static/readme-images/pages/buy-page-screenshot.webp "Buy Page")

The buy page displays a search button at the top. It is a simple search of caravan makes and models.

Below this, jinja templating loops through all the available listings and renders them in bootstrap cards. Each card displays some information relevant to the caravan. The user is invited to press the 'See More' button to display a more detailed view of the chosen caravan.

### Listing Page

![Listing Page](/static/readme-images/pages/listing-page-screenshot.webp "Listing Page")

![Listing Details](/static/readme-images/pages/listing-page-screenshot-details.webp "Listing Details")

This page displays more details of the chosen caravan. The user is invited to press the 'phone' or 'email' button to reveal the sellers contact details.

### About Page 

![About Page](/static/readme-images/pages/about-page-screenshot.webp "About Page")

![Directors Details](/static/readme-images/pages/about-page-screenshot-directors.webp "Directors Details")

The about page detail information about the history of the company as well as the background of the company's Directors.


### Register Page

![Register Page](/static/readme-images/pages/register-page-screenshot.webp "Register Page")

This page allows a user to input their details and register as a user, giving them access to create, edit and delete their own listings.

Their phone and email is a requirement as this will be accessible for buyers on their listing.

The route checks if a username already exists and redirects to the register page again if it's already taken.

Once registered, the user is redirect to the profile page in their dashboard. and the dashboard nav link becomes available to them. They will also have access to their listings through the dashboard.

The password is hash for security reasons.

### Login Page

![Login Page](/static/readme-images/pages/login-page-screenshot.webp "Login Page")

The login page is for users who have already registered. They simply enter their username and password to login in. 

There username is checked against the database and access is given to relevant pages and data.

Once logged in, they are redirected to their profile page in their dashboard.

## USER AREA

Once a user is logged on, they can access the following pages. This is due to a wrapper used to decorate routes relating to pages only logged in users can access.

### Dashboard View
Once logged in a user has access to a new menu item/nav link called dashboard. This takes the user through to their own unique dashboard with a side bar navigation to allow access to their profile and their own listings.

### Profile Page

![Profile Page](/static/readme-images/pages/profile-screenshot.webp "Profile Page")

![Edit Profile Page](/static/readme-images/pages/edit-profile-screenshot.webp "Edit Profile Page")

From here the user can edit their name and contact details. It was important to allow the user to update their contact details as these are available to buyers on the detailed listing page. 

Users are not allowed to edit their username. This is set when they register.

### User Listings

![Listings Page](/static/readme-images/pages/users-listings-screenshot.webp "Listings Page")

![Add Listing Page](/static/readme-images/pages/add-caravan-listing-screenshot.webp "Add Listing Page")

![Edit Listing Page](/static/readme-images/pages/edit-caravan-screenshot.webp "Edit Listing Page")

On first use, this page will be relatively empty. A user must add their first caravan listing using the 'add caravan' button. Once created, this view will show the user their caravan listings in table format and they have the ability to edit or delete their own listings via the ellipsis button.

## SUPER USER AREA

If a user is granted superuse priviledges via another superuser, they will have more menu items in the side navgation bar in the dashboard. This includes users and caravan details. Again this is achieved through a wrapper that decorates certain routes.

### Users

![Users Page](/static/readme-images/pages/users-screenshot.webp "Users Page")

![Edit User Page](/static/readme-images/pages/edit-users-screenshot.webp "Edit User Page")

This is a simple table that allows super users to grant other users superuser priviledges via a toggle button.

### Caravan Details

![Caravan Details Page](/static/readme-images/pages/caravan-details-screenshot.webp "Caravan Details Page")

![Details Dropdown Page](/static/readme-images/pages/caravan-details-dropdown-screenshot.webp "Details Dropdown Page")

This view brings you to an accordian style page of four dropdown menus for caravan make, model, features and location. It was decided that these inputs on the form fields to add or edit a caravan listings would be best suited to be pre-populated with correct industry items. This prevents mis-spellings of caravan makes and models, regulates features and is specific to location.

## ERROR HANDLERS

![Error Page](/static/readme-images/pages/error-page-screenshot.webp "Error Page")

A single page was created to handle several errors. The error handlers were created in app.py and pass the relevant message to the error page.

# TECHNOLOGIES USED
## Languages
* HTML5
* CSS3
* Javascript
* Python
## Framework
* Bootstrap v 5.3
* Flask
## Database
* MongoDB
## Tools
* Git
* GitHub
* Gitpod
* Balsamiq
* Google Fonts
* Font Awesome

# BUGS

## Fixed Bugs
| No. | Problem | Fix |
| --- | --- | --- |
| 1 | Links to edit and delete in listing cards not working | Remove card-overlay that was holding the price. The z-index was the problem. I could’ve reduced the size of the card-overlay, but I changed the location of the price as I preferred the look of it |
| 2 | Needed wrap decorator for only superuser access for certain pages | https://stackoverflow.com/questions/35407560/attributeerror-dict-object-has-no-attribute-predictors showed me how to access the key in the document. This is located in app.py def superuser_required(f): |

## Known Bugs
- The search feature only searches full words, for example a caravan make is swift, but if you only search for 'swi', it will come back as 'no results', but if you search for 'swift' all the caravans with the make swift will come back.
- Although the image upload input (when adding or editing a listing) is formatted to accept images and to filter your files by images. It is possible to manually override this and input something that is not an image. This is something I would like to work for future releases. 

# TESTING
Extensive testing was conducted and documented in [Testing.md](TESTING.md)

# WISHLIST

There are many ways this site could be developed in the future to have many more features. Here are some on my wishlist:

- Distinguish between trade and private sellers
- Allow upload and display of multiple images
- Provide a way for users to review listing owners
- See how many people have viewed an owners listing
- Pagination for the listings on the buy page and on dashboard tables
- The search feature only searches for make and model. In the future, I would like to expand this search to other fields.

# DEPLOYMENT

Heroku was use for deploying this app. These are the steps used for deployment to Heroku:

In GitPod CLI, the the root directoy of the project, run: pip3 freeze --local > requirements.txt to create a requirements.txt file containing project dependencies.
In the Gitpod project workspace root directory, create a new file called Procfile. Inside the Procfile, check that web: python3 app.py has been added when creating the file Save the file.

Login to Heroku, select Create new app, add a name for the app and choose the region closest to you.
go to the 'Deploy' tab on the Heroku dashboard and select Github, search for your repository and click 'connect'.
Navigate to the settings tab, click reveal config vars and input the the following:
Key	Value
* "IP", "0.0.0.0"
* "PORT", 5000
* "SECRET_KEY", "secret key"
* "MONGO_URI", "mongo db uri"
* "MONGO_DBNAME", "mongo db name"
* "CLOUD_NAME", "cloudinary name"
* "API_KEY", "api key"
* "API_SECRET", "secret key"

Go back to the Deploy tab and select enable automatic deploys. Click deploy branch and then open app once the build is complete.

Fork the repository by logging into Github and locating the repository. Click the Fork button in the top right corner. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link. In the terminal change the current working directory to the location you want to use for the cloned directory. Type git clone, and paste the URL you copied and press enter.

## Forking the Github Repository

* Login to Github and locate the repository
* Locate the 'Fork' button and click it
* A copy of the repository should now be in your account

## Cloning the Github Repository

* Login to Github and locate the repository
* Click on the 'code' button and 'download zip'
* Extract the zip file on your local machine
* Run the index.html file in a browser

# CREDITS

**Code Institute** - I thoroughly enjoyed learning python through Code Insitute and have used guiding principles from the course throughout this website.

**[Font Awesome](https://fontawesome.com/)** -  was used for the icons from the site and instructions were followed on how to install from their website.

**[Tiny PNG](https://tinypng.com/)** - was used to reduce the file size of each image.

**[Adobe Express](https://express.adobe.com/spv)** - was used to resize the images.

**[Google Fonts](https://fonts.google.com/)** - were the source for the fonts used throughout the site.

**[Online-Convert](https://image.online-convert.com/)** - was used to convert the files to webp.

**[Bootstrap](https://getbootstrap.com/docs/5.3/components/modal/)** - Was used for most of the styling and responsiveness.

**[Flask](https://getbootstrap.com/docs/5.3/components/modal/)** - Was used for most of the styling and responsiveness.

**[Jinja Templating](https://getbootstrap.com/docs/5.3/components/modal/)** - Was used for templating and template logic in the templates.

**[MongoDB](https://getbootstrap.com/docs/5.3/components/modal/)** - Was used for the database.

**[Heroku](https://getbootstrap.com/docs/5.3/components/modal/)** - Was used for deployment.

**[Am I Reponsive](https://ui.dev/amiresponsive)** - was used to create the first image in the readme file to show the responsiveness of the website.

**[Swift Caravan Details](https://www.swiftholidayhomes.co.uk/)** - Swift caravan images and text taken from this website for educational purposes only

**[Willerby Caravan Details](https://www.willerby.com/)** - Willerby caravan images and text taken from this website for educational purposes only

**[Delta Caravan Details](https://www.deltacaravans.co.uk/index.html)** - Delta caravan images and text taken from this website for educational purposes only

All other text and coding was created by myself.
