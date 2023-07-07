# Caravansy

![Image showing the Caravansy website on various devices](/static/readme-images/testing/responsive-home-screen.webp "Caravansy")

## FUNCTIONAL TESTING

| Test| Goal | Result |
| :--- | :--- | :--- |
| Responsiveness | App responsive across different device sizes | Pass |
| Flash Messages | Messages display in an obvious way to users | Pass |
| Search - No Results | Display flash message explaining no results | Pass |
| Choose caravan detail from dropdown list | Make, model, features and location chosen through dropdown list | Pass |
| Check navigation links | Navigation links render correct pages | Pass |
| Dashboard displays as expected | Sidebar links render correctly | Pass |
| Logged in user redirect correct | User redirected to profile page | Pass |
| Logged in user can access two dashboard pages | Access profile page and their listings page | Pass |
| Superusers see appropriate dashboard pages | Users and Caravan Details link available | Pass |

## Validators

### HTML Validation
All the pages of the site passed validation on W3S **[HTML Validator](https://validator.w3.org/)** except for a warning that the Buy Page section lacks a heading. However, the h3 header is a child of two divs.

![HTML Validation](/static/readme-images/testing/html-validation.webp "HTML Validation")

### CSS Validation
The style sheet passed validation with flying colours with W3S **[CSS Validator](https://jigsaw.w3.org/css-validator/)**

![CSS Validation](/static/readme-images/testing/css-validation.webp "CSS Validation")

### Javascript Validation
The javascript file passed validation with **[JSHint](https://jshint.com/)**

![Javascript Validation](/static/readme-images/testing/jshint-validation.webp "Javascript Validation")

### Pep8 Validation
The app.py python file passed validation using the **[CI Python Linter](https://pep8ci.herokuapp.com/#)**

![Python Validation](/static/readme-images/testing/pep8-validation.png "Python Validation")

### Lighthouse Testing
The website did well on the **[lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk)** tests. Best practices were a little lower, but this was due to a console.log error on my chrome developer tools. But this did not occur on others.

![Lighthouse Tests](/static/readme-images/testing/lighthouse-screenshot.webp "Lighthouse Tests")

### WAVE Accessibility Testing
The app did well with the **[WAVE](https://wave.webaim.org/)** accessibilty testing. It had two errors to begin with, declaring that the green 'sy' did not have enough contrast with the white background and the same with the sign in link. Therefore, a black background was given to both of these to resolve this.

![Accessibilty Tests](/static/readme-images/testing/wave-accessibility-screenshot.webp "Accessibilty Tests")

## User Story Testing
The following user stories were created as a basis for this project. See below how each one was achieved.

### User
As a user, I want to:

1. Browse caravan listings
    - An unregistered user is able to browse listings by navigating to the 'buy' page using the top navigation bar. They are able to view all available listings and also search specifically for the make or model they are looking for.

![View Listings](/static/readme-images/testing/user-stories/view-listings.webp "View Listings")

2. Know how to get in touch with the owner
    - Pressing the 'see more' button of a listing takes the user to a more detailed page of that specific caravan and allows the user to find out the email and phone number of the owner via pressing the 'email' or 'phone' buttons located on the right hand side of the screen on desktops.

![Contact Owner](/static/readme-images/testing/user-stories/contact-owner.webp "Contact Owner")

3. Be able to register
    - Using the top navigation bar, the user can click the link to 'register' and once this page has rendered, the user can enter the required informtion and submit their registration form. If all is done correctly, the user will be registered.

![Register](/static/readme-images/testing/user-stories/register.webp "Register")

4. Be able to list a caravan to sell
    - To list a caravan, a user must be registered and logged in. If a user attempts to use the link on the home page to 'list caravan', they are automatically redirected to the register page - which has some text explaining they must register to list.
    - If a user is already logged in, they can click on the home page 'list caravan' button and they will be directed to the page where they can add a listing.
    - Similarly, if they go to their dashboard and navigate using the sidebar to the listings, they can click on the 'add listing' button and are redirected to the page where they can add a listing.
    - On the add a listing page, they can fill in the required details for their caravan listing and submit it. Once this has been done, a document is created in the database and the caravan listing will be displayed in the 'buy' page section of the website.

![Add Caravan Listing](/static/readme-images/testing/user-stories/add-listing-home-button.webp "Add Caravan Listing")
![Add Caravan Listing](/static/readme-images/testing/user-stories/view-edit-personal-listing.webp "Add Caravan Listing")
![Add Caravan Listing](/static/readme-images/testing/user-stories/add-caravan-listing.webp "Add Caravan Listing")

5. View my listings
    - Once logged in, the user can navigate to the listing section of the sidebar in the dashboard section. Here, they can view a table of all their current listings and it is from here, they can individually edit or delete their listing.

![View Listing](/static/readme-images/testing/user-stories/view-personal-listings.webp "View Listing")
![Edit Listing](/static/readme-images/testing/user-stories/edit-caravan-listing.webp "Edit Listing")
![Delete Listing](/static/readme-images/testing/user-stories/delete-caravan-listing.webp "Delete Listing")

6. Change my details
    - Once logged in, the user can go to the profile page in their dashboard. Using the 'edit profile' button, they can change their personal information, except for their username as this is unique to them.

![View Profile](/static/readme-images/testing/user-stories/edit-profile-button.webp "View Profile")
![Edit Profile](/static/readme-images/testing/user-stories/edit-profile.webp "Edit Profile")

### Site Owner
As a site owner I want:
1. users to achieve the user stories listed above
    - see user stories above
2. to be able to turn certain users into superusers
    - The site owner is a superuser and is able to add others as superusers. The site owner does this by navigating to the 'users' section of their dashboard. This nav link and the relevant page it directs to is only accessible to superusers.
    - Once the superuser has navigated to the users page, they can see which users are superusers or not. 
    - To add someone as a superuser, they can click the green ellipsis box and then press edit. They are redirected to a page where they can toggle the user as a superuse or not.
    - From the ellipsis box on the 'users' page, the superuser can also delete users.

![View Users](/static/readme-images/testing/user-stories/view-users.webp "View Users")
![Edit Users](/static/readme-images/testing/user-stories/edit-users.webp "Edit Users")
![Toggle Superusers](/static/readme-images/testing/user-stories/toggle-users.webp "Toggle Superusers")

3. add, edit and delete certain caravan details
    - A superuser has access to the 'caravan details' link from the sidebar in the dashboard page.
    - Clicking this link takes the superuser to an accordion page where the superuser can drop down each detail to see the current categories under it.
    - The superuser make create a new category for a detail by clicking the 'add' button to the side of the detail heading.
    - The superuser may edit individual categories under each detail by clicking the ellipsis button to the right of each detail name and then clicking edit.
    - The superuser may delete individual categories under each detail by clicking the ellipsis button to the right of each detail name and then clicking delete. It was decided as this was not based on a relational model, that deleting a category would not automatically delete listings that included that category. It just stops a user using that category in future. This is so that a caravan listing that is using an older model won't be deleted because that reference no longer exists.

![View Caravan Details](/static/readme-images/testing/user-stories/caravan-details-page.webp "View Caravan Details")
![Details View](/static/readme-images/testing/user-stories/ellipsis-caravan-details.webp "Details View")
![Add Caravan Details](/static/readme-images/testing/user-stories/add-caravan-detail.webp "Add Caravan Details")
![Edit Caravan Details](/static/readme-images/testing/user-stories/edit-caravan-details.webp "Edit Caravan Details")
![Delete Caravan Details](/static/readme-images/testing/user-stories/delete-caravan-details.webp "Delete Caravan Details")