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
    - [`Wireframes`](#wireframes)
    - [`Colour`](#colour)
    - [`Typography`](#typography)
    - [`Code Structure`](#code-structure)
    - [`Structure`](#structure)
- [`Features`](#features)
    - [`Home Page`](#home-page)
    - [`Game Page`](#game-page)
    - [`End Page`](#end-page)
    - [`404 Error`](#404-error)
- [`Technologies Used`](#technologies-used)
    - [`Languages`](#languages)
    - [`Framework`](#framework)
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

The about page detail information about the history of the comnpany as well as the background of the company's Directors.


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

