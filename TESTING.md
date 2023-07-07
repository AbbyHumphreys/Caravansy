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

