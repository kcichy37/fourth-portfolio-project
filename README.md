# BARBER

## Purpose of the project
purpose of the project is to build a Full-Stack site based on business logic used to control a centrally owned dataset. Project has an authentication mechanism and provides role-based access to the site's data or other activities based on the dataset.

The barber shop uses a database to build a booking logic for a business need of controling datasets of customers bookings information. Both the customer and admin are able to Create, Read, Update and Delete these datasets.
![Responsive](/static/assets/images/readme/responsive.PNG "Responsive")

## User Stories
### 1) Visiting User
- As a visiting user, I want to be able to find out information such as opening times, address and services provided by the business.
- As a visiting user, I want to be able to register on the site for bookings.
- As a visiting user, I want to be able to contact the business. 

### 2) Registered User
- As a registered user, I want to be able book a chosen service at a desired time and date and with my chosen barber.
- As a registered user, I want to be able to view my bookings and know if they have been approved.
- As a registered user, I want to be able to edit my bookings in case of wrong input or change of availability.
- As a registered user, I want to be able to delete my bookings.

### 3) Admin
- As an admin, I want to be able to create new bookings on the system.
- As an admin, I want to be able to view every users bookings and the details of the booking.
- As an admin, I want to be able to edit customers information if needed be.
- As an admin, I want to be able to delete bookings.
- As an admin, I want to be able to view customers queries and their contact information. 

## Features
### Header/Nav-bar
- The navbar is a feature that is on every page, it consists 4 links and the Barber name. Home and Barber are both linked to index.html, Service and Contact us are linked accordingly with their ID's so when clikced they scroll down to the respresentative section on the index.html. 4th link is the Login which takes you to the login page.
- For unregistered user's the navbar consists 4 links, whereas if you're registed it consits of extra Booking link, My booking link and instead of a login link, there's, a logout link.
![Logged in navbar](/static/assets/images/readme/logged_in_navbar.PNG "Logged in navbar")
- When links are hovered over they turn dark green for user to recognise they are hovering over the link. 
![NavBar](/static/assets/images/readme/navbar.PNG "NavBar") ![NavBar-green](/static/assets/images/readme/navbar-green.PNG "NavBar-green")
- The navbar is responsive and when the width size is decrease the navbar toggles a burger button, which when pressed shows a list of the links.
![Burger navbar](/static/assets/images/readme/burger.PNG "Burger navbar")

### Picture Carousel
- The home page has a picture carousel with 3 images, it changes the pictures by itself, but in addition it has buttons for user to change picuters.
![Picture Carousel](/static/assets/images/readme/piccar1.PNG "Picture Carousel")![Picture Carousel](/static/assets/images/readme/piccar2.PNG "Picture Carousel")![Picture Carousel](/static/assets/images/readme/piccar3.PNG "Picture Carousel")

### Information and Google maps
- Under the picture carousel there's a little section with the key business details such as, where to find us, how to get in touch and opening times.
- Besides all this information theres iframe of google maps and pin-pointed location where the barber shop is located.
![Details And iframe](/static/assets/images/readme/details_iframe.PNG "Details And iframe")

### Service's provided by the Barber shop 
- The services that the business provides are presented in cards with pictures of the service accompanied by a title and price
- At the bottom of the service section there's a book button. however if user is not signed in that book button is a log in button.
![Services](/static/assets/images/readme/services.PNG "Services")

### Contact us
- The contact details are highlighted in the details area, however at the bottom of the home page theres a form for any user to fill out with their query 
- The form requires a Name, Surname, Email, and the Query, if these are not filled out then the form cannot be submitted.
![Contact us](/static/assets/images/readme/Contact_us.PNG "Contact us")

### Footer
- Footer is on every page, with simple social media icons that lead to represantitve social media.

### Login/Register/logout
- The login/register/logout form have been provided by the django-allauth add on, they are presented on the page in a minimalistic form.
![Login](/static/assets/images/readme/login.PNG "Login")![Resgister](/static/assets/images/readme/Register.PNG "Resgister")![Sign out](/static/assets/images/readme/signout.PNG "Sign out")

### Booking page
- Booking page is a simple booking form for the user to fill out, once filled out and all required fields are filled out the submition will take user to their booking page.
![Booking](/static/assets/images/readme/booking.PNG "Booking")

### My bookings
- My bookings page consists of two sections the Approved booking section and Pending bookings section 
- Approved bookings only show in approve section once Admin approves the pending booking
![Approved](/static/assets/images/readme/Approved_booking.PNG "Approved")
- Pending booking show straight after a booking is made
![Pending](/static/assets/images/readme/Pending_booking.PNG "Pending")
- Bookings are presented in a card form with details such as date of booking, time, barber and service. 
- Pending bookings have ability to delete a booking and edit a booking, whereas accepted booking only have the ability to cancel a booking.
