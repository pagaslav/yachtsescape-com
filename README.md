# Yachtsescape README

![Responsive Mockup](docs/images/respons/respons-mockup.webp)

View the live site [here](https://yachtsescape-a7b4e5d759f6.herokuapp.com/)

## Introduction

Welcome to YachtsEscape, your premier destination for discovering and booking luxury yacht rentals. Our platform is designed to provide users with an effortless experience, from searching for the perfect yacht to securing your booking. Whether you're planning a tranquil getaway or an adventurous voyage, YachtsEscape.com offers a wide selection of yachts to suit every preference.

## Project Goals

The primary goal of YachtsEscape.com is to make yacht rentals accessible and straightforward for both users and administrators. Our objectives include:

1. **User-Friendly Yacht Search**: Provide a seamless search experience for users, allowing them to find available yachts quickly and easily by filtering results based on location, date, price, and other preferences.

2. **Streamlined Booking Process**: Ensure that users can book yachts effortlessly, with a clear and intuitive process that includes instant booking confirmations and secure payment options.

3. **Comprehensive Yacht Information**: Offer detailed and accurate information about each yacht, including photos, specifications, and user reviews, helping users make informed decisions.

4. **Efficient Account Management**: Empower users to manage their accounts effectively, including access to booking history, saved yachts, and personalized settings, ensuring a personalized experience.

5. **Proactive User Engagement**: Keep users engaged with notifications about new yachts, special offers, and promotions, encouraging them to return and explore more options regularly.

6. **Robust Admin Tools**: Equip administrators with the tools they need to manage yacht listings, user accounts, bookings, and payments efficiently, maintaining the accuracy and integrity of the platform.

7. **Reliable Reporting and Analytics**: Provide administrators with comprehensive reporting features to analyze user activity, booking trends, and financial transactions, enabling data-driven decisions for platform improvement.

Our mission is to create a platform that not only simplifies the yacht rental process but also enhances the overall experience for both users and administrators, ensuring a smooth and enjoyable journey from search to booking.

## User Stories

### First Time Visitor Goals:

1. As a first-time visitor, I want to quickly grasp what **YachtsEscape.com** is all about so that I can start exploring yacht rental options without feeling lost.
2. When I first visit the site, I’m looking for a straightforward way to search for available yachts by location and date. It’s important that the process is easy and intuitive so that I can find the perfect yacht without any hassle.
3. I want to dive into detailed information about each yacht, including photos, specifications, and reviews, so I can confidently choose the one that best suits my needs.
4. I’m curious about the company itself—its background, guarantees, and customer service approach—because knowing more about who I’m dealing with makes me feel more secure in my decision.
5. I need to easily find the company’s contact information and location. Whether I have a question or need to visit, I want this information to be readily accessible.

### Returning Visitor Goals:

1. As a returning visitor, I want to log back in and pick up where I left off, whether it’s continuing my search, reviewing yachts I’ve already looked at, or finalizing a booking.
2. It’s important to me that I can quickly rebook a yacht I’ve rented before. I don’t want to start the search from scratch every time I visit.
3. I want to manage my wishlist easily—keeping track of yachts I’m interested in and getting alerts if their availability or price changes.
4. Staying updated is key for me. I want to subscribe to updates about new yacht listings and special offers so that I don’t miss out on something exciting.

### Registered User Goals:

1. As a registered user, I appreciate getting notifications about new yachts, discounts, and promotions, so I can stay ahead of the curve and book the best deals.
2. I want to be able to manage my account settings and preferences without any hassle, ensuring that everything is tailored to what I’m looking for.
3. Having quick access to my booking history is important. It’s helpful to review past rentals or quickly rebook a yacht I enjoyed.

### Admin Goals:

As the site admin, I’m responsible for making sure everything runs smoothly:

1. I need to keep the yacht listings up to date, adding new ones and editing or removing outdated information to ensure users always see accurate options.
2. Managing user accounts is a big part of my job. I need to be able to view, edit, and, if necessary, delete user profiles to maintain the platform’s integrity.
3. I oversee all bookings—viewing, modifying, or canceling them as needed to help users and keep things organized.
4. Tracking and managing payments is crucial. I make sure all transactions are processed correctly and address any payment issues that arise.
5. To understand how well the platform is performing, I generate reports on user activity, bookings, and payments, which helps me make informed decisions about future improvements.

## MoSCoW Prioritization

I used MoSCow prioritization to organize each iteration of my project.

### Must Have

- **Design and implement a relational data model**: I'll need to design the database structure that fits the needs of the yacht rental service, making sure it can store, manage, and manipulate all relevant data.
  
- **Authentication, authorization, and permission features**: It’s essential that I handle who can log in, what they can do, and protect sensitive areas of the site. I’ll be making sure that only authorized users can make bookings or manage content.

- **E-commerce payment system**: I'll implement a payment system that allows users to securely book and pay for yacht rentals directly through the site.

- **Use version control (Git) and deploy to the cloud**: I’m documenting everything in Git, making regular commits, and hosting the project on a cloud platform like Heroku.

### Should Have

- **Full-stack web app using Django**: I’ve designed a multi-app Django project with a relational database and user interactions.

- **Accessible and user-friendly front-end**: I'm ensuring the site is designed with accessibility in mind and provides a smooth user experience.

- **Forms for users**: I'll have forms with validation, allowing users to submit and edit information easily.

- **Clean code**: I'll make sure the code follows Django conventions and is easy to maintain.

- **Custom Python logic**: I'll include Python functions with logic like loops and conditions to handle the yacht rental process and bookings efficiently.

- **Testing**: I'll run tests to check that everything works properly—from responsiveness to data management.

- **Database design**: I've created a database schema that shows clear relationships between yachts, users, and bookings.

- **CRUD functionality**: I'll provide the ability to create, read, update, and delete records like yachts and bookings, making sure the system works smoothly for both admins and users.

### Won’t Have

- **Referral system**: This feature is something I’m skipping for now, as it’s not critical to the core of the project.

## Project Setup
### 1. Commitizen Setup
- Installed **Commitizen** and **cz-customizable** for standardized commit messages.
- Created and configured `.cz-config.js` to define commit types and scopes.

### 2. Virtual Environment
- Created a virtual environment for the project to manage dependencies.
- Added the `env` directory to `.gitignore` to prevent tracking of the virtual environment files.

### 3. Django Installation
- Installed **Django** version 5.1.1 to start developing the application.

### 4. Project Initialization
- Began the project setup for YachtsEscape.com, aimed at providing a platform for yacht rentals.

#### Running the Django Application

To start the Django application, follow these steps:

1. **Activate the Virtual Environment:**
   Make sure your virtual environment is activated. Run the following command:

   - **For Windows:**
     ```bash
     .\env\Scripts\activate
     ```

   - **For macOS and Linux:**
     ```bash
     source env/bin/activate
     ```

2. **Run the Development Server:**
   Once the virtual environment is activated, you can start the Django development server with the following command:

   ```bash
   python3 manage.py runserver

## User Experience (UX) & User Interface (UI)

### Wireframes

<details>
<summary>Home Page</summary>

![Home Page](docs/images/wireframes/home-page.png)
</details>

<details>
<summary>Log in Page</summary>

![Log in Page](docs/images/wireframes/login-page.png)
</details>

<details>
<summary>Sign Up Page</summary>

![Sign Up Page](docs/images/wireframes/sign-up-page.png)
</details>

<details>
<summary>Our Fleet Page</summary>

![Our Fleet Page](docs/images/wireframes/our-fleet-page.png)
</details>

<details>
<summary>About Us Page</summary>

![About Us Page](docs/images/wireframes/about-page.png)
</details>

<!-- <details>
<summary>Privacy Policy Page</summary>

![Privacy Policy Page](documentation/wireframes/privacy-polisy-page.webp)
</details> -->

<details>
<summary>Profile Page</summary>

![Profile Page](docs/images/wireframes/profile-page.png)
</details>

<details>
<summary>Yacht management Page</summary>

![Yacht management Page](docs/images/wireframes/yachts-management-page.png)
</details>

<details>
<summary> Yacht Detail Page</summary>

![Yacht Detail Page](docs/images/wireframes/yacht-detail-page.png)
</details>

<details>
<summary>Booking success Page</summary>

![Booking success Page](docs/images/wireframes/booking-success-page.png)

</details>
<summary>Map of website</summary>

![Map of website](docs/images/wireframes/site-map.webp)

</details>

### Colour Scheme

#### Color Palette
The color palette for YachtsEscape was chosen to give the site a clean, professional look, while keeping it tied to the theme of yachting. Here are the main colors:

- **Primary Color:** #088cdc (Light Blue) – Inspired by the sea, this color feels fresh and calm. It's used for buttons, icons, and other important elements to give the site a bright, welcoming feel.
- **Secondary Color:** #006bb3 (Deep Blue) – This darker blue adds depth and trust. It's used for the logo, hover states, and interactive elements.
- **Text Color:** #444444 (Dark Grey) – Used for main body text, this grey keeps things readable without being too harsh.
- **Background Color:** #f8f8f8 (Light Grey) – A soft, neutral background that lets the content shine without being distracting.
- **White:** Mainly used for text on dark backgrounds like the footer and image sections, creating strong contrast for easy reading.
- **Footer Background:** #000000 (Black) – The footer uses black to make the white text stand out and give the site a solid base.

#### Visual Harmony and Accessibility
- **Contrast and Readability:** High contrast between text and background ensures everything is easy to read. The white text on dark sections like the footer improves visibility.
- **Balance:** Blue dominates the design, while grey and white keep the layout clean and focused.
- **Consistency:** The color scheme is consistent throughout, reinforcing the brand identity and making navigation intuitive.
- **Accessibility:** The colors meet accessibility standards, ensuring the site is usable for everyone, including those with visual impairments.

![Colour Palette](docs/images/ux/color-palette.webp)

#### Visual Harmony and Accessibility

- **Contrast and Readability**: Ensure there is sufficient contrast between the primary color (Green) and the accent color (White) for text and important elements to maintain readability.
- **Balance**: Use soft orange sparingly to highlight key actions without overwhelming the natural and calm aesthetic of the site.
- **Consistency**: Maintain a consistent use of colors throughout the website to create a harmonious visual experience that supports the site’s calming and professional atmosphere.
- **Accessibility**: Consider accessibility guidelines, ensuring that all text is readable by maintaining an appropriate contrast ratio and using color combinations that are friendly for users with color vision deficiencies. This includes testing the color palette with accessibility tools to verify compliance with WCAG standards.

### Typography

The primary font used throughout the site is [**Lato**](https://fonts.google.com/specimen/Lato), a Google Font, chosen for its clean and modern look, ensuring readability across all devices. It comes in various weights (100, 300, 400, 700, 900) to give flexibility in styling headings, body text, and other elements.

![Lato Google Font](docs/images/ux/lato-google.webp)

For icons, I use [**Font Awesome**](https://fontawesome.com/), which adds clarity and visual appeal to buttons, social media links, and navigation elements.

### YachtsEscape Logo

The **YachtsEscape** logo features a sleek, modern design with a minimalist illustration of a yacht, combined with bold typography. The yacht symbol uses a clean blue (#088cdc) color, which represents the ocean, aligning with the overall maritime theme of the website. The bold black text beside the yacht adds a professional touch, making the brand name stand out clearly.

There are two variations of the logo:

- **Light Version**: This version is used against dark backgrounds, such as in the initial state of the header and in the footer of the website.
- **Dark Version**: This version appears against lighter backgrounds, such as when the user scrolls down and the header becomes fixed on a white background.

![YachtsEscape Dark Logo](docs/images/ux/logo-dark.png)
![YachtsEscape Light Logo](docs/images/ux/logo-light.webp)

The logo dynamically changes between these versions based on the user's scroll position and screen width, enhancing the website's aesthetic and functionality.

Below is the JavaScript code that switches between the light and dark versions of the logo as the user interacts with the page:

```javascript, static/js/base.js
// Function to change the logo based on scroll position and window width
function updateLogo() {
    let windowWidth = $(window).width();
    let scrollTop = $(window).scrollTop();
    let lightLogo = $("#logo").data("light-logo");
    let darkLogo = $("#logo").data("dark-logo");
    let smallLightLogo = $("#logo").data("small-light-logo");
    let smallDarkLogo = $("#logo").data("small-dark-logo");

    if (scrollTop > scrollTrigger) {
        // Change logo to dark version based on screen size
        if (windowWidth < 689) {
            console.log("Switching to small dark logo:", smallDarkLogo);
            $("#logo").attr("src", smallDarkLogo);
        } else {
            console.log("Switching to dark logo:", darkLogo);
            $("#logo").attr("src", darkLogo);
        }
    } else {
        // Change logo to light version based on screen size
        if (windowWidth < 689) {
            console.log("Switching to small light logo:", smallLightLogo);
            $("#logo").attr("src", smallLightLogo);
        } else {
            console.log("Switching to light logo:", lightLogo);
            $("#logo").attr("src", lightLogo);
        }
    }
}
```

## Features

### Navigation
The navigation panel of Yachtsescape rental website is designed to provide a user-friendly and intuitive browsing experience.

#### Navbar
The Navbar is composed of two main parts: the **Top Bar** and the **Main Navigation**.



##### Top Bar
The **Top Bar** provides quick access to essential contact information and social media links:

![Desktop Navigation](docs/images/navigation/nav-desctop.webp)

- **Phone and Email**: 
  - Users can quickly dial the phone number or email YachtsEscape with one click from the top bar.
  - These contact options are visible on all screen sizes, ensuring accessibility.
  
- **Social Media Links**: 
  - Links to Twitter, Facebook, Instagram, and YouTube are available, each opening in a new window. The icons are styled using FontAwesome and aligned on the right of the top bar for convenience.

##### Main Navigation
The **Main Navigation** is designed to be responsive and intuitive:

![Desktop Navigation after Scrolling](docs/images/navigation/nav-desctop-scroll.webp)

- **Brand Logo**: 
  - The logo is positioned on the left side of the navbar, dynamically changing based on scrolling. When the user scrolls past 50px, the logo transitions from light to dark (or small versions on mobile), thanks to the custom JavaScript code in `base.js`.

- **Menu Behavior**: 
  - The menu adapts responsively, converting into an off-canvas (sidebar) menu on smaller devices. The menu's hamburger icon becomes visible on mobile devices, ensuring the navigation is accessible across screen sizes.
  
- **Dynamic Menu Based on User Status**:
  - If the user is authenticated, an account dropdown is displayed with links to profile for all users and management pages for admin users.

![Desktop Dropdown Menu (1)](docs/images/navigation/nav-desctop-drop-1.webp)

  - If the user is not authenticated, a **Sign In** button appears instead.

![Desktop Navigation with Sign In](docs/images/navigation/nav-desctop-signin.webp)

- **Yacht Fleet Menu**: 
  - The **Our Fleet** section is a dropdown that categorizes yachts by type (Leisure, Fishing, Celebrations), allowing users to filter yachts according to their preferences.

![Desktop Dropdown Menu (2)](docs/images/navigation/nav-desctop-drop-2.webp)

- **Book Now Button**: 
  - A prominent **Book Now** button is available, leading to a modal with a booking form. This form allows users to filter yachts by type, capacity, and availability using intuitive date pickers.

![Desktop Navigation with Book Now Button](docs/images/navigation/nav-desctop-book-now.webp)

##### Layout and Responsiveness

- The **Main Navigation** and **Top Bar** are designed to collapse elegantly on smaller screens, with all elements accessible via the off-canvas sidebar.

![Tablet Navigation](docs/images/navigation/nav-tablet.webp)
![Mobile Navigation](docs/images/navigation/nav-mobile.webp)

- The **Logo**, **Menu Items**, and **Book Now** button are designed to shift layout based on screen size, ensuring a consistent and responsive experience for users on all devices.

![Tablet Navigation with Menu](docs/images/navigation/nav-tablet-menu.webp)
![Mobile Navigation with Menu](docs/images/navigation/nav-mobile-menu.webp)

The navigation ensures quick access to essential services and an intuitive flow, enhancing the user journey across the site.

##### Desktop View:

![Desktop View](documentation/navbar/desktop-navbar.webp)

##### Responsive Design:

##### Tablet View:

![Tablet View](documentation/navbar/tablet-close-navbar.webp)
![Tablet View](documentation/navbar/tablet-open-navbar.webp)

##### Mobile View:

![Mobile View](documentation/navbar/mob-close-navbar.webp)
![Mobile View](documentation/navbar/mob-open-navbar.webp)

### Footer

The footer section of our website is designed to provide essential information and easy access to our social media channels. Below is a detailed description of its features and layout across different devices:

##### Desktop View:

![Desktop View](documentation/footer/footer-desktop.webp)

- **Logo and Company Name**: 
  - Located on the left side of the footer, the company logo and name, "THE KNEE SURGERY," are prominently displayed.

- **Contact Information**: 
  - In the center, visitors can find our contact details:
    - **Address**: 456 Side Street, Cardiff, CF19 6FY
    - **Email**: theknee.surgery@gmail.com

- **Social Media Icons**: 
  - To the right, icons for Instagram, Facebook, Twitter, and YouTube are displayed, providing quick links to our social media profiles.

- **Copyright and Privacy Policy**:
  - At the bottom, it states: "© 2024 Artem Bryzh. All rights reserved." 
  - A link to the Privacy Policy is also provided.

##### Responsive Design:

##### Tablet View:

![Tablet View](documentation/footer/footer-tablet.webp)

- **Logo and Company Name**: 
  - Located centrally.

- **Contact Information**:
  - Positioned centrally with the same details as the desktop view.

- **Social Media Icons**:
  - Aligned below the contact information, allowing easy access.

- **Back to Top Arrow**:
  - A convenient back-to-top arrow is present, aiding navigation.

##### Mobile View:

![Mobile View](documentation/footer/footer-mob.webp)

- **Logo and Company Name**: 
  - The company logo and name remain at the top, positioned centrally, ensuring brand visibility.

- **Contact Information**: 
  - Centrally aligned for easy reading.

- **Social Media Icons**: 
  - Arranged below the contact information in a horizontal layout.

- **Back to Top Arrow**:
  - Located at the bottom right corner, this arrow aids in easy navigation back to the top of the page.

The footer is designed to be responsive and user-friendly across all devices, ensuring that visitors can easily find contact information and access our social media channels, no matter the device they are using.

### Home Page
Welcome to The Knee Surgery homepage, designed with user experience and functionality in mind. Here’s a breakdown of its features:

![Home Page](documentation/pages/home-page-full.webp)

- **Introduction Section**: 
  - Contains a brief overview of our commitment to knee surgery and patient care.
  - Includes two prominent buttons for easy navigation: "Our Doctors" and "About Us"

- **Future Interactive Image**: 
  - A placeholder image that will be interactive in future updates, enhancing user engagement and providing more information visually.

- **Comprehensive List of Services**:
  - **Initial Consultation and Diagnosis**: Personalized assessment plans.
  - **Arthroscopic Surgery**: Minimally invasive procedures.
  - **Knee Replacement**: Advanced techniques and implants.
  - **Ligament Reconstruction**: Restoring knee stability.
  - **Physical Therapy and Rehabilitation**: Customized exercise programs.
  - **Injection Procedures**: Non-surgical pain management options.

### Log In Page
The Log In page allows users to access their accounts on The Knee Surgery website. The page includes the following features:

![Log In Page](documentation/pages/login-page-full.webp)

1. **Email Input**: Users enter their email address in a floating label input field.
2. **Password Input**: Users enter their password in a floating label input field.
3. **Remember Me Checkbox**: Users can choose to stay logged in for 30 days.
4. **Sign In Button**: Submits the form to log in the user.
5. **Sign Up Link**: Redirects new users to the sign-up page.
6. **Forgot Password**: Provides the administrator's email for password reset assistance.

When the "Sign In" button is clicked, the user's credentials are validated on the backend. If the credentials are correct, the user is logged in; otherwise, a flash message indicates incorrect email or password.

![Log In Incorrect](documentation/pages/login-page-incorrect.webp)

The "Remember Me" checkbox is processed on the backend. The backend code uses Flask session management to keep the user logged in if the checkbox is selected.

      ```python
      from flask import session

      # Session configuration
      app.config["SESSION_PERMANENT"] = False  # Session is not permanent by default
      app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=30)

      if existing_user:
              # Set session to be permanent if remember me is checked
              if remember:
                  # This sets the session to use the permanent lifetime
                  session.permanent = True
                  # Set session lifetime to 30 days
                  app.permanent_session_lifetime = timedelta(days=30)
      ```

Clicking on the administrator’s email opens the mail program with the “To” field filled out. 

### Sign Up Page
The sign-up page allows new users to create an account on The Knee Surgery website. The form includes client-side validation using JavaScript to ensure the password meets the criteria and matches the confirmation password. The backend handles additional validation, password hashing, and user creation.

![Sign Up Page](documentation/pages/signup-page-full.webp)

The page includes the following features:

1. **Full Name Input**: Users enter their full name in a floating label input field.
2. **Gender Selection**: Users select their gender from a dropdown list.
3. **Date of Birth Input**: Users enter their date of birth in a floating label input field.
4. **Phone Number Input**: Users enter their phone number, which must be between 9 to 11 digits. JavaScript handles input changes to show or hide a sample text.
5. **Email Input**: Users enter their email address in a floating label input field.
6. **Password Input**: Users create a password with requirements displayed below the input field. The password must be at least 8 characters long, contain an uppercase letter, and a number. JavaScript validates the password in real-time. Gray check marks turn green as each requirement is met.

![All marks are neutral](documentation/pages/signup-page-password-1.webp)

![One mark is green](documentation/pages/signup-page-password-2.webp)

![Two marks are green](documentation/pages/signup-page-password-3.webp)

![All marks are green](documentation/pages/signup-page-password-4.webp)

7. **Confirm Password Input**: Users confirm their password. JavaScript ensures that both password fields match. Each password field includes a Font Awesome eye icon that toggles password visibility when clicked.

![Visibility](documentation/pages/signup-page-password-5.webp)

8. **Terms and Conditions Checkbox**: Users must agree to the terms and conditions. Clicking the link opens a modal with the terms for review.

![Terms and Conditions](documentation/pages/signup-page-terms.webp)

Users must agree to the terms and conditions. Without checking this box, users cannot complete the registration.

![Terms and Conditions agree](documentation/pages/signup-page-terms-checkbox.webp)

On the backend, the following occurs:

- **Email Validation**: The backend checks if the email is already registered.
- **Password Validation**: The backend ensures the passwords match and meet the requirements.
- **Password Hashing**: The password is hashed using `generate_password_hash`.
- **User Creation**: A new user record is created and saved in the database.
- **Session Handling**: The user's email is added to the session to log them in automatically.

### Privacy Policy Page
The Privacy Policy page provides detailed information about how The Knee Surgery website collects, uses, and protects user data. It is a crucial component for informing users about their privacy rights and the measures taken to safeguard their information. 

<details>
<summary>See Privacy policy Page</summary>

![Privacy Policy Page](documentation/pages/policy-page-full.webp)
</details><br>
  
The policy includes sections on:

- **Data Collection**: Explains what personal data is collected, such as email addresses, names, phone numbers, and usage data.
- **Usage of Data**: Describes how the collected data is used to provide and improve services.
- **Cookies and Tracking**: Details the use of cookies and other tracking technologies to enhance user experience.
- **Data Sharing**: Outlines conditions under which user data may be shared with third parties.
- **Data Security**: Ensures the protection of personal data, though it acknowledges no method is 100% secure.
- **Children’s Privacy**: States the service does not address users under 13 and the measures taken if such data is inadvertently collected.
- **External Links**: Advises users to review privacy policies of linked websites not operated by The Knee Surgery.
- **Policy Changes**: Notifies users that the Privacy Policy may be updated and the process for informing users of changes.

This Privacy Policy was generated and adapted using the [Privacy Policy Generator](https://www.termsfeed.com/privacy-policy-generator/).

### Our Doctors Page
The "Our Doctors" page features images and brief information about our doctors, including their specialties and experience. This page dynamically updates with new doctors added by the admin through a for loop, ensuring the latest information is always displayed.

![Our Doctors Page](documentation/pages/our-doctors-page-full.webp)

The page layout includes:

- **Doctor Image**: Displays the doctor's image if available; otherwise, a default image is shown.
- **Doctor Information**: Presents the doctor's name, specialty, description, and additional information.

The page structure is generated automatically from the database entries using the following template code snippet:

      ```html
      {% for doctor in doctors %}
      <div class="col-12">
        <div class="card mb-3">
          <div class="row g-0">
            <div class="col-md-4">
              <img
                src="{{
                  url_for('static', filename=get_image_path(doctor.image)) 
                  if doctor.image else
                  url_for('static', filename='images/default-doctor.webp') 
                }}"
                class="img-fluid rounded-start"
                alt="{{ doctor.name }}">
            </div>
            <div class="col-md-8">
              <div class="card-body">
                <h3 class="card-title">{{ doctor.name }}</h3>
                <p class="card-text">{{ doctor.specialty }}</p>
                <p class="card-text">{{ doctor.description }}</p>
                <p class="card-text-hide">{{ doctor.additional_info }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      {% endfor %}
      ```

### About us Page
The "About Us" page for The Knee Surgery website provides comprehensive information about the clinic, its history, and its commitment to providing high-quality orthopedic care.

- **Introduction**
  - A welcoming message with a brief history and the clinic's dedication to patient satisfaction and medical excellence.

![About Us Page](documentation/pages/about-us-page-full.webp)

- **Carousel Section**
  - A Bootstrap carousel showcasing four key areas of the clinic:
    1. **Reception at Our Clinic**: Warm and inviting environment for patients.
    2. **Our Hospital Corridor**: Modern and convenient clinic facilities.
    3. **Operating Theatre**: Equipped with the latest medical technology.
    4. **Hospital Room**: Comfortable and modern environment for patients.

For optimal viewing experience, different images are used for various screen sizes, ensuring clarity and quality on all devices.

**Detailed Descriptions**
  - **Our Journey**: The history of the clinic and its growth over the past decade.
  - **Our Commitment to Quality**: Focus on personalized treatment plans and understanding patient needs.
  - **Patient Satisfaction**: Testimonials and the dedication of the staff to provide excellent care.
  - **Continuous Improvement**: Ongoing training and certification programs for doctors.
  - **Our Community**: Involvement in the local community through health fairs and educational seminars.
  - **Looking to the Future**: Commitment to innovation and expanding services.

As we continue to grow and evolve, we are excited to share that we have plans to enhance our “About Us” page further. In the near future, we aim to include testimonials from our patients, offering firsthand accounts of their experiences and the positive impact our clinic has had on their lives. These testimonials will provide valuable insights and reinforce the trust and satisfaction our patients feel.

Additionally, we will be showcasing our certifications and achievements in the medical field. By highlighting the qualifications and accolades of our dedicated team, we aim to demonstrate our commitment to excellence and continuous improvement. These additions will give visitors a more comprehensive understanding of our clinic’s dedication to providing exceptional orthopedic care.

### Profile Page

#### Patient Profile Page

The patient profile page on our website offers a comprehensive view of the patient's personal information, medical records, and appointment management. Here is an overview of what the patient can do and see on this page:

![Patient Profile Page](documentation/pages/profile-patient-page.webp)

##### Key Sections:

1. **User Information**
   - **Name:** Displays the patient's name, with an option to edit.
   - **Role:** Shows the user's role as a patient.
   - **Phone:** Shows the patient's phone number, with an option to edit.
   - **Email:** Displays the patient's email, with an option to edit.
   - **Gender:** Shows the patient's gender.
   - **Date of Birth:** Displays the patient's date of birth.

2. **Change Password**
   - Patients can change their password by providing the current password and setting a new one, ensuring it meets security requirements.

3. **Medical Records**
   - **List of Medical Records:** Displays detailed information about the patient's medical history, including descriptions, treatments, dates, and the attending doctor's details.
   - **Download and Delete Files:** Patients can view, download, and delete their uploaded files related to their medical records.

4. **Scheduled Appointments**
   - **View Scheduled Appointments:** Displays the list of upcoming appointments with doctors, including the doctor's name, reason for the visit, and scheduled date and time.

5. **Requested Appointments**
   - **List of Appointment Requests:** Shows the appointments that the patient has requested, including the reason and current status of each request.

6. **Request an Appointment**
   - **Form to Request Appointments:** Allows patients to request new appointments by providing the reason for the visit.

This page is designed to be user-friendly, providing patients with easy access to their medical information and appointment management tools.

#### Admin Profile Page

The admin profile page on our website is designed to provide a comprehensive set of tools for managing user information, medical records, and appointments. Here's a breakdown of the key features and functionalities available to administrators:

![Admin Profile Page](documentation/pages/profile-admin-page.webp)

##### Key Sections:

1. **User Information**
   - **Name:** Displays the admin's name with an option to edit.
   - **Role:** Shows the user's role as an admin, with the ability to edit.
   - **Phone:** Displays the admin's phone number, which can be edited.
   - **Email:** Shows the admin's email address, with an option to update it.
Administrators have enhanced privileges within the system. They can edit any information in their own profile or in any profile they view without needing to input the current password.

2. **Change Password**
   - Admins can securely change their password by entering the current password and setting a new one, ensuring it meets security requirements.

3. **Appointment Requests**
   - **List of Appointment Requests:** Displays all pending appointment requests from patients, including the patient's name and the reason for the appointment.
   - **Assign Doctor:** Allows admins to assign doctors to specific appointment requests, facilitating efficient scheduling and management.

4. **Admin-Specific Actions**
   - **View All Users:** A button that navigates to a page where admins can view and manage all users and doctors in the system.
   - **Add a New Doctor:** A button that links to a form where admins can add new doctors, expanding the clinic's team.

5. **Uploaded Files**
   - **Manage Files:** Admins can view, download, and delete uploaded files related to patient records, ensuring all relevant documents are easily accessible.
   - **Upload Documents:** Provides a form for uploading new documents, with options to categorize the file type (e.g., medical record, analysis, profile picture, or other).

The admin profile page is designed to give administrators full control over the system, ensuring efficient management of user information, medical records, and appointments. This comprehensive toolset helps maintain the high standards of care and service at our clinic.

#### Doctor Profile Page

The doctor profile page on our website is designed to provide doctors with the tools and information they need to manage their patient interactions, appointments, and medical records efficiently. Here's a detailed overview of the key features and functionalities available to doctors:

![Doctor Profile Page](documentation/pages/profile-doctor-page.webp)

##### Key Sections:

1. **User Information**
   - **Name:** Displays the doctor's name with an option to edit.
   - **Role:** Shows the user's role as a doctor.
   - **Phone:** Displays the doctor's phone number, which can be edited.
   - **Email:** Shows the doctor's email address, with an option to update it.
   - **Specialty:** Displays the doctor's specialty, which can be updated to reflect their expertise.

2. **Change Password**
   - Doctors can securely change their password by entering the current password and setting a new one, ensuring it meets security requirements.

3. **Assigned Patients**
   - **List of Assigned Patients:** Displays all patients assigned to the doctor, including patient names, reasons for appointments, and symptoms.
   - **Accept and Schedule Appointments:** Allows doctors to accept and schedule appointments, providing fields for the appointment date and time.
   - **Medical Records:** Doctors can view and access the medical records of their assigned patients, ensuring they have all the necessary information for consultations.

4. **Medical Records Management**
   - **View Medical Records:** Provides detailed information about patients' medical records, including descriptions, treatments, and dates.
   - **Add Medical Record:** Doctors can add new medical records for their patients, documenting treatments, descriptions, and dates.

The doctor profile page is designed to give doctors full control over their interactions with patients, ensuring efficient management of patient information, medical records, and appointments. This comprehensive toolset helps maintain the high standards of care and service at our clinic.

### Appointment Request and Scheduling Workflow on Profile Page
This section describes the complete workflow for requesting and scheduling an appointment within the Knee Surgery application. It details the steps from a patient requesting an appointment to a doctor scheduling it, including the roles of the patient, admin, and doctor.

#### Step-by-Step Process:

1. **Patient Requests an Appointment:**
   - **Action:** The patient fills out the "Request an Appointment" form, specifying the reason for the appointment.

   ![Request an Appointment](documentation/pages/appointment/request-patient-1.webp)

   - **Interface:** The patient clicks the "Request Appointment" button.

   ![Click the button](documentation/pages/appointment/request-patient-2.webp)

2. **Page Reload and Confirmation:**
   - **Action:** Upon clicking the button, the page reloads.
   - **Interface:** The requested appointment appears in the patient's profile under the "Requested Appointments" section.

   ![Requested Appointments](documentation/pages/appointment/requested-patient.webp)

3. **Database Update:**
   - **Action:** The appointment request is added to the `theknee_surgery.appointments` collection in MongoDB.
   - **Details:** The new appointment entry includes a status of `pending`.

   ![MongoDB status of `pending`](documentation/pages/appointment/request-mongo-1.webp)

4. **Admin Views Appointment Request:**
   - **Action:** In the admin profile, the new appointment request is visible under the "Appointment Requests" section.
   - **Interface:** The request includes the patient's name, reason for the appointment, and an option to assign a doctor.

   ![Appointment Requests for admin](documentation/pages/appointment/request-admin.webp)

5. **Admin Assigns a Doctor:**
   - **Action:** The admin selects a doctor from a dropdown menu and clicks the "Assign Doctor" button.

   ![Assigns a Doctor](documentation/pages/appointment/assign-admin.webp)

   - **Database Update:** The status of the appointment in MongoDB changes from `pending` to `assigned`.

   ![MongoDB status of `assigned`](documentation/pages/appointment/assign-mongo.webp)

   - **Interface:** The appointment request is removed from the admin's "Appointment Requests" section and appears in the assigned doctor's profile under the "Assigned Patients" section.

   ![Assigned Patients for doctor](documentation/pages/appointment/assigned-doctor-1.webp)

6. **Doctor Schedules the Appointment:**
   - **Action:** The doctor selects a date and time for the appointment and clicks the "Accept and Schedule" button.

   ![Accept and Schedule](documentation/pages/appointment/assigned-doctor-2.webp)

   - **Database Update:** The status of the appointment in MongoDB changes to `scheduled`.

   ![MongoDB status of `scheduled`](documentation/pages/appointment/sheduled-mongo.webp)

7. **Updated Views for Doctor and Patient:**
   - **Doctor's Profile:**
   - **Interface:** The scheduled appointment remains in the "Assigned Patients" section.

   ![Assigned Patients](documentation/pages/appointment/assigned-doctor-3.webp)

   - **Patient's Profile:**
   - **Interface:** The appointment is moved from the "Requested Appointments" section to the "Scheduled Appointments" section with the assigned date and time.

   ![Scheduled Appointments](documentation/pages/appointment/sheduled-patient.webp)

### Database Collection:

- **Collection:** `theknee_surgery.appointments`
  - **Fields:**
    - `patient_id`: Reference to the patient requesting the appointment.
    - `doctor_id`: Reference to the doctor assigned to the appointment.
    - `reason`: Reason for the appointment.
    - `status`: Status of the appointment (`pending`, `assigned`, `scheduled`).
    - `appointment_datetime`: Date and time when the appointment is scheduled (added during the scheduling step).

### Workflow Summary:

1. **Patient Action:** Requests an appointment.
2. **System Action:** Adds request to database with status `pending`.
3. **Admin Action:** Assigns a doctor, changing status to `assigned`.
4. **Doctor Action:** Schedules the appointment, changing status to `scheduled`.
5. **Patient and Doctor Views:** Updated to reflect the current status and details of the appointment.

This workflow ensures a seamless process for managing appointment requests, assignments, and scheduling within the Knee Surgery application.


### All Users Page
The "All Users" page is an administrative tool that provides a detailed overview of all users registered on the website. This page is accessible exclusively to administrators and serves as a central hub for user management. Below is a detailed description of the features and functionalities available on the All Users page:

![All Users Page](documentation/pages/admin-users-page.webp)

#### Key Features:

1. **User List Overview:**
   - **Sorted Display:** The page displays all users in a sorted order, starting with administrators, followed by doctors, and then patients. This helps in quickly identifying and managing users based on their roles.
   - **User Information:** Each entry includes the user's full name and role, with a link to view their profile for more detailed information.

2. **Flash Messages:**
   - **Notifications:** The page includes a section for flash messages to notify the admin of the success or failure of various actions, such as password resets or user deletions.

3. **User Actions:**
   - **Reset Password:** Administrators can reset a user's password by generating a new random password, which is hashed and updated in the database. The new password is displayed to the admin for further communication to the user. This feature is particularly useful if a user forgets their password and requests access recovery.
   - **Delete User:** Administrators have the ability to delete any user from the system. This action requires confirmation to prevent accidental deletions.

#### User Management Workflow:

- **Accessing the Page:** The "All Users" page is linked from the admin's profile page, making it easily accessible for user management tasks.
- **Viewing Profiles:** Admins can click on a user's name to view their detailed profile, which provides more context and information about the user.
- **Performing Actions:** Admins can reset passwords or delete users directly from the All Users page, with appropriate confirmation prompts to ensure deliberate actions.

### Add Doctor Page
The "Add Doctor" page is a crucial tool for administrators to manage the medical staff at The Knee Surgery clinic. This page is exclusively accessible through the admin's profile and allows the admin to add new doctors to the database. Once added, these doctors are automatically displayed on the "Our Doctors" page.

![Add Doctor Page](documentation/pages/add-doctor-page.webp)

1. **Bootstrap Form:**
   - **User-Friendly Design:** The page features a Bootstrap form designed to be intuitive and user-friendly, ensuring that admins can quickly and easily add new doctors.

2. **Form Fields:**
   - **Full Name:** A required input field for the doctor's full name.
   - **Specialty:** A required input field for the doctor's specialty.
   - **Description:** A required textarea for a brief description of the doctor's role and activities.
   - **Additional Information:** An optional textarea for more detailed information about the doctor. This section is hidden on screens smaller than 600 pixels to ensure a clean and responsive design.
   - **Email:** A required input field for the doctor's email address.
   - **Password:** A required input field for setting the doctor's password.

3. **Backend Integration:**
   - **Form Submission:** When the form is submitted, the backend processes the input data. This includes validating the entries, hashing the password for security, and generating an image name based on the doctor's full name.
   - **Database Update:** The new doctor's information is saved to the MongoDB database, and the doctor is immediately added to the "Our Doctors" page.

4. **Security and Permissions:**
   - **Admin-Only Access:** The page and its functionalities are restricted to users with admin privileges. Non-admin users attempting to access the page are redirected with a permission error message.

### Medical Records Page
The Medical Record page is a comprehensive tool designed for doctors and admin users to manage and update patient medical records efficiently. This page provides a detailed view of the patient's medical history and allows for the upload and management of associated documents.

![Medical Record Page](documentation/pages/medical-record-page.webp)

#### Key Features:

1. **Flash Messages:**
   - **User Notifications:** At the top of the page, flash messages are displayed to inform users about the success or failure of their actions, such as updates or deletions.

2. **Medical Record Details:**
   - **Patient Information:** The patient's name is displayed in a read-only format.
   - **Record Date:** An input field for the date of the medical record.
   - **Description:** A textarea for the description of the medical record, pre-filled with existing data.
   - **Treatment:** A textarea for the treatment details, pre-filled with existing data.
   - **Update Button:** If the logged-in user is either the doctor assigned to the record or an admin, they can update the medical record.

3. **Uploaded Files Section:**
   - **List of Files:** Displays all files uploaded related to the medical record. Each file has a download link and a delete button.
   - **Delete Functionality:** Admins and the assigned doctor can delete any file associated with the medical record.

4. **Upload Document Section:**
   - **File Upload:** Allows users to upload new documents related to the medical record.
   - **Form Submission:** The form supports file uploads and sends the data to the backend for processing and storage.

#### Page Workflow:

- **Viewing Medical Records:** The page displays detailed information about a patient's medical history, including dates, descriptions, and treatments.
- **Uploading Files:** Users can upload new documents, such as test results or additional notes, to be associated with the medical record.
- **Updating Records:** Authorized users can update the medical record's details to reflect new information or changes in treatment.
- **Managing Files:** Users can view, download, or delete files that have been uploaded to the medical record.

### 404 Page
The **404 Page Not Found** is a user-friendly error page that is displayed when a user attempts to access a page that does not exist on the website. This page aims to inform users clearly and provide them with an easy way to navigate back to the homepage.

![404 Page](documentation/pages/404-page.webp)

#### Key Features:

1. **Title:**
   - **Page Title and subtitle:** The title of the page and subtitle is "404 The page you are looking for does not exist." making it immediately clear what the issue is.

2. **Content:**
   - **Error Code:** The page prominently displays the error code "404" in a large font size to catch the user's attention.
   - **Message:** A simple message informs the user that the page they are looking for does not exist.
   - **Navigation Button:** A button is provided to take the user back to the homepage, encouraging them to continue browsing the site.

#### Page Workflow:

- **User Interaction:** When a user lands on this page, they are informed of the error and given a clear option to return to the homepage.
- **Navigation:** The primary call-to-action is to direct the user back to a familiar place where they can continue their navigation without frustration.

### 403 Page
The **403 Forbidden** page is shown when a user attempts to access a page or resource they do not have permission to view. This could be due to various reasons, such as insufficient user privileges or restricted content.

![403 Page](documentation/pages/403-page.webp)

#### Key Features:

1. **Title:**
   - **Page Title and subtitle:** The title and subtitle of the page is "403 You do not have permission to access this page." clearly indicating the nature of the access issue.

2. **Content:**
   - **Error Code:** The error code "403" is displayed prominently in a large font size.
   - **Message:** A straightforward message informs the user that they do not have permission to access the requested page.
   - **Navigation Button:** A button is provided to return the user to the homepage, guiding them away from the restricted area.

#### Page Workflow:

- **User Interaction:** Users are immediately informed about the permission issue and are not left wondering why they cannot access the page.
- **Navigation:** The page encourages users to return to the homepage, providing a positive direction instead of a dead end.

## Database Design

The project uses MongoDB for its database, structured to handle various aspects such as user management, appointments, and medical records. MongoDB's flexible schema is ideal for managing dynamic medical data.

### Collections

#### Users Collection

This collection stores the details of all users registered in the system. By default, all users are patients upon registration. An admin can change a user's role to either doctor or admin.

| Field      | Type     | Description                           |
|------------|----------|---------------------------------------|
| `_id`      | ObjectId | Unique identifier for each user       |
| `name`     | String   | Name of the user                      |
| `gender`   | String   | Gender of the user                    |
| `dob`      | Date     | Date of birth                         |
| `phone`    | String   | Contact number                        |
| `email`    | String   | Email address                         |
| `password` | String   | Hashed password                       |
| `role`     | String   | Role of the user (`patient` or `admin`) |

#### Doctors Collection

This collection stores the details of all doctors registered in the system.

| Field            | Type     | Description                              |
|------------------|----------|------------------------------------------|
| `_id`            | ObjectId | Unique identifier for each doctor        |
| `name`           | String   | Name of the doctor                       |
| `role`           | String   | Role of the user (`doctor`)              |
| `specialty`      | String   | Medical specialty                        |
| `description`    | String   | Description of the doctor's expertise    |
| `additional_info`| String   | Additional information about the doctor  |
| `image`          | String   | Image name                               |
| `password`       | String   | Hashed password                          |
| `email`          | String   | Email address                            |
| `dob`            | Date     | Date of birth                            |
| `gender`         | String   | Gender of the doctor                     |
| `phone`          | String   | Contact number                           |

#### Appointments Collection

Stores appointment requests and schedules.

| Field                 | Type       | Description                                              |
|-----------------------|------------|----------------------------------------------------------|
| `_id`                 | ObjectId   | Unique identifier for each appointment                   |
| `patient_id`          | ObjectId   | Reference to the patient                                 |
| `reason`              | String     | Reason for the appointment                               |
| `status`              | String     | Status of the appointment (`pending`, `assigned`, `scheduled`) |
| `assigned_doctor_id`  | ObjectId   | Reference to the assigned doctor                         |
| `date_requested`      | Date       | Date when the appointment was requested                  |
| `appointment_datetime`| Date       | Scheduled date and time for the appointment              |
| `doctor_email`        | String     | Email address of the doctor                              |
| `doctor_name`         | String     | Name of the doctor                                       |

#### Medical Records Collection

Stores medical records associated with patients.

| Field        | Type       | Description                           |
|--------------|------------|---------------------------------------|
| `_id`        | ObjectId   | Unique identifier for each record     |
| `patient_id` | ObjectId   | Reference to the patient              |
| `doctor_id`  | ObjectId   | Reference to the doctor               |
| `description`| String     | Description of the medical condition  |
| `treatment`  | String     | Treatment provided                    |
| `date`       | Date       | Date of the record                    |

#### Medical Record Files Collection

Stores files associated with medical records.

| Field        | Type       | Description                           |
|--------------|------------|---------------------------------------|
| `_id`        | ObjectId   | Unique identifier for each file       |
| `record_id`  | ObjectId   | Reference to the medical record       |
| `file_id`    | String     | Cloudinary file ID                    |
| `file_url`   | String     | URL to access the file                |
| `file_name`  | String     | Name of the file                      |
| `uploaded_at`| Date       | Date when the file was uploaded       |

#### User Files Collection

Stores files uploaded by patients and admins.

| Field        | Type       | Description                           |
|--------------|------------|---------------------------------------|
| `_id`        | ObjectId   | Unique identifier for each file       |
| `user_id`    | ObjectId   | Reference to the user                 |
| `file_id`    | String     | Cloudinary file ID                    |
| `file_url`   | String     | URL to access the file                |
| `file_name`  | String     | Name of the file                      |
| `file_type`  | String     | Type of file (e.g., medical record)   |
| `uploaded_at`| Date       | Date when the file was uploaded       |

### Reason for Separate File Collections

Separate collections for user-uploaded files and doctor-uploaded files in medical records help in:

1. **Organizational Clarity**: Better organization and management of data by clearly separating user and doctor files.
2. **Access Control**: Different access permissions can be applied to user files and medical record files.
3. **Audit and Tracking**: Improved tracking and auditing of file uploads by users and doctors.
4. **Data Integrity**: Ensures that medical records remain consistent and are not accidentally altered by user uploads.

### User Roles and Registration

- **Patients**: All users are registered as patients by default.
- **Admins**: Admins can be assigned by directly modifying their role in the database.
- **Doctors**: Doctors can be assigned by either modifying their role directly in the database or by an admin through the web interface when adding a new doctor.

This database design allows for efficient management of user data, medical records, appointments, and associated files, providing a comprehensive structure for the application.

### Entity Relationship Diagram

![ERD My DB](documentation/erd-mongodb.webp)

## Technologies Used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) was used as the foundation of the site.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/css) - was used to add the styles and layout of the site.
- [Bootstrap](https://getbootstrap.com/docs/5.3) was employed to integrate its styles, facilitating rapid development and
consistent styling across the pages.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) was employed to implement dynamic interactions on the site, enabling real-time user feedback and interactive features without needing to reload the page.
- [jQuery](https://jquery.com/) used for user interaction on the site.
- [Python](https://www.python.org/)  is used as the back-end programming language.
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) is the Python framework used for the site.
- [MongoDB](https://www.mongodb.com/) is the non-relational database management I chose to use for storing data.
- [VSCode](https://code.visualstudio.com/) was used as the main tool to write and edit code.
- [Git](https://git-scm.com/) was used for the version control of the website.
- [GitHub](https://github.com/) was used to host the code of the website.
- [Heroku](https://dashboard.heroku.com/apps)  is hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com/) used for online static file storage.
- [Balsamiq](https://balsamiq.com/) was used to make wireframes for the website.
- [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop.html) was used to make and resize images for the website and the
README file.
- [ICO Converter](https://www.icoconverter.com/) - for the favicon.
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) - was used to debug, to test responsiveness and generate Lighthouse reports.
- [Google Fonts](https://fonts.google.com/) - to import the site font.
- [Font Awesome](https://fontawesome.com/) - for all the site icons.
- [W3C HTML Validator](https://validator.w3.org/) - to test HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator) - to test the CSS code.
- [JSHint](https://jshint.com/) is a tool used to detect errors and potential problems in JavaScript code.

## Testing

### Responsiveness

<details>
<summary>Home Page</summary>

![Home Page](documentation/pages/responsiv/home-page-responsive.webp)
</details>

<details>
<summary>Log in Page</summary>

![Log in Page](documentation/pages/responsiv/login-page-responsive.webp)
</details>

<details>
<summary>Sign Up Page</summary>

![Sign Up Page](documentation/pages/responsiv/signup-page-responsive.webp)

With the opened Modal window:

![Sign Up Page with Modal](documentation/pages/responsiv/signup-1-page-responsive.webp)
</details>

<details>
<summary>Our Doctors Page</summary>

![Our Doctors Page](documentation/pages/responsiv/doctors-page-responsive.webp)
</details>

<details>
<summary>About Us Page</summary>

![About Us Page](documentation/pages/responsiv/about-page-responsive.webp)
</details>

<details>
<summary>Privacy Policy Page</summary>

![Privacy Policy Page](documentation/pages/responsiv/privacy-page-responsive.webp)
</details>

<details>
<summary>Profile Page</summary>

Patient

![Profile Page Patient](documentation/pages/responsiv/profil-patient-page-responsive.webp)

Admin

![Profile Page Admin](documentation/pages/responsiv/profil-admin-page-responsive.webp)

Doctor

![Profile Page Doctor](documentation/pages/responsiv/profil-doctor-page-responsive.webp)
</details>

<details>
<summary>Add Doctor Page</summary>

![Add Doctor Page](documentation/pages/responsiv/add-doctor-page-responsive.webp)
</details>

<details>
<summary>All Users Page</summary>

![All Users Page](documentation/pages/responsiv/all-users-page-responsive.webp)
</details>

<details>
<summary> Medical Records Page</summary>

![Medical Records Page](documentation/pages/responsiv/medical-record-page-responsive.webp)
</details>

<details>
<summary> 404 Page</summary>

![404 Page](documentation/pages/responsiv/404-page-responsive.webp)
</details>

<details>
<summary> 403 Page</summary>

![403 Page](documentation/pages/responsiv/403-page-responsive.webp)
</details>

### Validator testing

#### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) to validate my Python file - app.py.

<details>

<summary> All clear, no errors found. See the screenshot</summary>

![404 Page](documentation/validator/ci-python-liner.webp)
</details>

#### HTML
I have used the recommended [HTML W3C Validator](https://validator.w3.org/) to validate all of my HTML files.

<details>
<summary>Home Page, no errors</summary>

![Home Page](documentation/validator/home-page-valid.webp)
</details>

<details>
<summary>Log in Page, no errors</summary>

![Log in Page](documentation/validator/login-page-valid.webp)
</details>

<details>
<summary>Sign Up Pag, no errorse</summary>

![Sign Up Page](documentation/validator/signup-page-valid.webp)

</details>

<details>
<summary>Our Doctors Page, no errors</summary>

![Our Doctors Page](documentation/validator/doctors-page-valid.webp)
</details>

<details>
<summary>About Us Page, no errors</summary>

![About Us Page](documentation/validator/about-page-valid.webp)
</details>

<details>
<summary>Privacy Policy Page, no errors</summary>

![Privacy Policy Page](documentation/validator/policy-page-valid.webp)
</details>

<details>
<summary>Profile Page, no errors</summary>

Patient

![Profile Page Patient](documentation/validator/profile-patient-page-valid.webp)

Admin

![Profile Page Admin](documentation/validator/profile-admin-page-valid.webp)

Doctor

![Profile Page Doctor](documentation/validator/profile-doctor-page-valid.webp)
</details>

<details>
<summary>Add Doctor Page, no errors</summary>

![Add Doctor Page](documentation/validator/add-doctor-page-valid.webp)
</details>

<details>
<summary>All Users Page, no errors</summary>

![All Users Page](documentation/validator/all-users-page-valid.webp)
</details>

<details>
<summary> Medical Records Page, no errors</summary>

![Medical Records Page](documentation/validator/medical-records-page-valid.webp)
</details>

<details>
<summary> 404 Page, no errors</summary>

![404 Page](documentation/validator/404-page-valid.webp)
</details>

<details>
<summary> 403 Page, no errors</summary>

![403 Page](documentation/validator/403-page-valid.webp)
</details>

#### CSS
I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/) to validate my CSS code.

![CSS Validation](documentation/validator/css.webp)

#### JavaScript
I have used the recommended [JShint Validator](https://jshint.com/) to validate my JS file.

![JS Validation](documentation/validator/js-valid.webp)

### LightHouse report

#### Home Page

<details>
<summary>Desktop</summary>

![Home Page Desktop](documentation/lighthouse/index-d.webp)
</details>
<details>
<summary>Mobile</summary>

![Home Page Mobile](documentation/lighthouse/index-m.webp)
</details>

#### Log in Page

<details>
<summary>Desktop</summary>

![Log in Page Desktop](documentation/lighthouse/login-d.webp)
</details>
<details>
<summary>Mobile</summary>

![Log in Page Mobile](documentation/lighthouse/login-m.webp)
</details>

#### Sign Up Page

<details>
<summary>Desktop</summary>

![Sign Up Page Desktop](documentation/lighthouse/signup-d.webp)
</details>
<details>
<summary>Mobile</summary>

![Sign Up Page Mobile](documentation/lighthouse/signup-d.webp)
</details>

#### Our Doctors Page

<details>
<summary>Desktop</summary>

![Our Doctors Page Desktop](documentation/lighthouse/doctors-d.webp)
</details>
<details>
<summary>Mobile</summary>

![Our Doctors Page Mobile](documentation/lighthouse/doctors-m.webp)
</details>

#### About Us Page

<details>
<summary>Desktop</summary>

![About Us Page Desktop](documentation/lighthouse/about-d.webp)
</details>
<details>
<summary>Mobile</summary>

![About Us Page Mobile](documentation/lighthouse/about-m.webp)
</details>

#### Privacy Policy Page

<details>
<summary>Desktop</summary>

![Privacy Policy Page Desktop](documentation/lighthouse/policy-d.webp)
</details>
<details>
<summary>Mobile</summary>

![Privacy Policy Page Mobile](documentation/lighthouse/policy-m.webp)
</details>

#### Profile Page

##### Patient's Profile Page

<details>
<summary>Desktop</summary>

![Patient Profile Page Desktop](documentation/lighthouse/profile-patient-d.webp)
</details>
<details>
<summary>Mobile</summary>

![Patient Profile Page Mobile](documentation/lighthouse/profile-patient-m.webp)
</details>

##### Admin's Profile Page

<details>
<summary>Desktop</summary>

![Admin Profile Page Desktop](documentation/lighthouse/profile-admin-d.webp)
</details>
<details>
<summary>Mobile</summary>

![Admin Profile Page Mobile](documentation/lighthouse/profile-admin-m.webp)
</details>

##### Doctor's Profile Page

<details>
<summary>Desktop</summary>

![Doctor Profile Page Desktop](documentation/lighthouse/profile-doc-d.webp)
</details>
<details>
<summary>Mobile</summary>

![Doctor Profile Page Mobile](documentation/lighthouse/profile-doc-m.webp)
</details>

#### Add Doctor Page

<details>
<summary>Desktop</summary>

![Add Doctor Page Desktop](documentation/lighthouse/add-doc-d.webp)
</details>
<details>
<summary>Mobile</summary>

![Add Doctor Page Mobile](documentation/lighthouse/add-doc-m.webp)
</details>

#### All Users Page

<details>
<summary>Desktop</summary>

![All Users Page Desktop](documentation/lighthouse/all-users-d.webp)
</details>
<details>
<summary>Mobile</summary>

![All Users Page Mobile](documentation/lighthouse/all-users-m.webp)
</details>

#### Medical Records Page

<details>
<summary>Desktop</summary>

![Medical Records Page Desktop](documentation/lighthouse/med-rec-d.webp)
</details>
<details>
<summary>Mobile</summary>

![Medical Records Page Mobile](documentation/lighthouse/med-rec-m.webp)
</details>

#### 404 Page

<details>
<summary>Desktop</summary>

![404 Page Desktop](documentation/lighthouse/404-d.webp)
</details>
<details>
<summary>Mobile</summary>

![404 Page Mobile](documentation/lighthouse/404-m.webp)
</details>

#### 403 Page

<details>
<summary>Desktop</summary>

![403 Page Desktop](documentation/lighthouse/index-d.webp)
</details>
<details>
<summary>Mobile</summary>

![403 Page Mobile](documentation/lighthouse/index-m.webp)
</details>

### Compatibility
In order to confirm the correct functionality, responsiveness, and
appearance:

- The website was tested on the following browsers: Chrome, Firefox,
Safari.

| Browser tested | Intended appearance | Intended responsiveness |
| - | - | - |
| Chrome | Good | Good |
| FireFox | Good | Good |
| Safari | Good | Good |

#### Chrome

<details>
<summary>Home Page Chrome</summary>

![Chrome. Index page](documentation/pages/home-page-full.webp)
</details>

#### Firefox

<details>
<summary>Home Page Firefox</summary>

![Firefox. Index page](documentation/pages/fire-shot-firefox-index-full.webp)
</details>

#### Safari

<details>
<summary>Home Page Safari</summary>

![Safari. Index page](documentation/pages/safari-index-full.webp)
</details>


### Manual Testing

For manual testing documentation, please continue to [TEST_SUITE_MANUAL.md](TEST_SUITE_MANUAL.md)

### Bugs

#### SSL

**SSL Certificate Verification Failed When Connecting to MongoDB:** Encountered an SSL certificate verification error (SSL: CERTIFICATE_VERIFY_FAILED) when trying to connect to MongoDB.

![Bug 1, code](documentation/bugs/1/bug-1.jpg)
![Bug 1, Error Message](documentation/bugs/1/bug-1-1.jpg)

**Solution:** Resolved the issue by adding the certifi library (import certifi) and modifying the PyMongo initialization line to specify the tlsCAFile parameter.

**Code Changes and Result:**

![Bug 1, Code Changes](documentation/bugs/1/bug-1-2.jpg)
![Bug 1, Result](documentation/bugs/1/bug-1-3.jpg)

#### Logout Issue

**Problem:**
When a user clicks the "Log Out" link and confirms the logout, the user is redirected to the homepage, but the navigation menu still shows the logged-in state (i.e., it still shows "Profile" and "Log Out" instead of "Log In" and "Sign Up"). Additionally, the user can still access the profile page.
**Steps to Reproduce:**

1.  Log in to your account.
2.  Click the "Log Out" link.
3.  Confirm the logout.
    **Cause:**
    The issue was caused by the JavaScript code for the logout not being correctly executed within the context of the Flask application, leading to the user session not being properly terminated on the server side. This issue is specific to how Jinja templates are rendered and how JavaScript interacts with the Flask backend.
    Initially, the JavaScript code for the logout was included in a custom JavaScript file. This caused the problem as described because the Jinja templating was not correctly interacting with the external JavaScript file. Once the code was moved directly into the `base.html` template, everything worked as expected.
    **Solution:**
    Ensure the JavaScript code is included at the right place in the `base.html` template to properly interact with the Flask backend:

            ```html
            <!-- Inline script for logout modal -->
            <script>
              $(document).ready(function () {
                // Attach a click event handler to the confirmLogout button
                $("#confirmLogout").click(function () {
                  // Redirect the user to the logout URL
                  window.location.href = "{{ url_for('logout') }}"
                })
              })
            </script>
            ```

After implementing the above solution, the logout functionality works as expected, with the user being properly logged out and the navigation menu updating correctly to reflect the logged-out state.

#### User Email Update Issue

**Problem:**
When a user updates their email address in the profile settings, the user remains logged in with the new email address, but they are redirected to the home page. Upon returning to the profile page, the user’s profile information is displayed correctly, but a “User not found” notification appears at the top of the page.

**Steps to Reproduce:**

    1.	Log in to your account.
    2.	Go to the profile page.
    3.	Click the “Edit” button to enable editing mode.
    4.	Change the email address to a new valid email address.
    5.	Enter the current password and click “Save.”
    6.	Observe the redirection to the home page.
    7.	Navigate back to the profile page.
    8.	Observe the “User not found” notification at the top of the page.

**Expected Behavior:**

    •	The user should remain on the profile page after updating the email address.
    •	No “User not found” notification should appear if the profile information is displayed correctly.

**Actual Behavior:**

    •	The user is redirected to the home page after updating the email address.
    •	A “User not found” notification appears at the top of the profile page upon returning.

**Screenshot:**
![Bug 3, User not found Message](documentation/bugs/3/bug-3-1.webp)

**Cause:**
The issue was caused by the Flask application not correctly updating the session and redirecting after an email change. Although the session email was updated, the redirection logic did not reflect the new session state, leading to the user being treated as unauthenticated or non-existent in subsequent requests.

**Solution:**
Ensure that after updating the email in the session, the user is redirected correctly and the session state is fully updated:

      ```python
      # Update session email if changed
      if current_email != new_email:
          session["user"] = new_email
          flash("Your email has been updated to {}.".format(new_email), "success")
          return {"success": True, "message": "Your email has been updated.", "redirect": url_for("profile", username=new_email)}
      else:
          flash("Your information has been updated.", "success")
          return {"success": True, "message": "Your information has been updated.", "redirect": url_for("profile", username=current_email)}
      ```

Ensure the JavaScript handles the success response correctly:

      ```javascript
      success: function (response) {
        if (response.success) {
          alert(response.message);
          window.location.href = response.redirect; // Updated to redirect after successful email change
        } else {
          alert(response.message);
        }
      }
      ```

After implementing the above solution, the email change functionality works as expected, keeping the user authenticated with the new email address and displaying the appropriate success message on the profile page.

![Bug 3, Result](documentation/bugs/3/bug-3-2.webp)

### Unsolved Bugs

To the best of my knowledge, there are no unresolved bugs at the
moment.

### Mistakes

- As I reached the end of this project, I realized the immense benefits of incorporating Agile methodologies for large-scale projects. Agile's iterative approach, flexibility, and focus on collaboration can significantly enhance project management and delivery.

- I plan to dive deeper into Agile practices starting today, right after I submit this project. By adopting Agile techniques, I aim to improve my workflow and better handle complex projects in the future.

- Initially, failed to document encountered bugs promptly during the coding process.
- Realised the importance of documenting bugs in real-time for better tracking and resolution.

- In future projects, I commit to maintaining a detailed log of encountered bugs and their resolution steps throughout the development process.

## Commit Conventions
This project uses [Commitizen](https://github.com/commitizen/cz-cli) to standardize commit messages. The majority of the commits have been made using `git cz`, which helps in maintaining a consistent commit history.

To make a commit using Commitizen, run:
```bash
git cz
```

## Deployment
The live site is deployed with Heroku; it can be accessed [here](https://theknee-surgery-f5b49706e9d6.herokuapp.com/).

### MongoDB Non-Relational Database

This project uses [MongoDB](https://www.mongodb.com/) for the Non-Relational Database.

To obtain your own MongoDB Database URI, sign-up on their site, then follow these steps:

#### Database Setup

1. The database in MongoDB should be named `insert-your-database-name-here`.
2. The necessary collection(s) for this database should be named `insert-your-collection-names-here`.

#### Connecting to MongoDB

1. Click on the name of the Cluster created for the project.
2. Click the `Connect` button.
3. Select `Connect Your Application`.
4. Copy the connection string, replace `<password>` with your actual password, and remove the angle brackets.

### Deployment to Heroku

1. **Create a New App**
   - Log into your Heroku Dashboard.
   - Click `New` in the top-right corner and select `Create new app`.
   - Enter a unique app name, select a region (EU or USA), and click `Create App`.

2. **Set Environment Variables**
   - Go to the `Settings` tab of your new app.
   - Click `Reveal Config Vars` and set the following variables:

   | Key                      | Value                  |
   | ------------------------ | ---------------------- |
   | IP                       | 0.0.0.0                |
   | PORT                     | 5000                   |
   | SECRET_KEY               | your_secret_key        |
   | MONGO_URI                | your_mongo_uri         |
   | MONGO_DBNAME             | your_mongo_dbname      |
   | CLOUDINARY_CLOUD_NAME    | your_cloudinary_cloud_name |
   | CLOUDINARY_API_KEY       | your_cloudinary_api_key |
   | CLOUDINARY_API_SECRET    | your_cloudinary_api_secret |

**Heroku requires three additional files for deployment**:

- `requirements.txt`
- `Procfile`
- `runtime.txt`

3. **Prepare Files for Heroku**

   - Create a `Procfile`:

     ```sh
     echo web: python app.py > Procfile
     ```

     Replace `app.py` with the name of your main Flask app file.

4. **Install Project Requirements**

   - Ensure all required packages are listed in `requirements.txt`:

     ```sh
     pip3 freeze --local > requirements.txt
     ```


5. **Deploying to Heroku**

   **Option 1: Automatic Deployment**

   - From your Heroku app dashboard, select the option for Automatic Deployment and follow the instructions.

   **Option 2: Manual Deployment via Terminal**

   - Log in to Heroku:

     ```sh
     heroku login -i
     ```

   - Set the Heroku remote repository:

     ```sh
     heroku git:remote -a your_app_name
     ```

   - Deploy your code:

     ```sh
     git push heroku main
     ```

Your project should now be connected and deployed to Heroku.

### Integrating Cloudinary for File Upload and Deletion

To add file upload and deletion functionality, we used Cloudinary. Among other services like Google and Amazon, Cloudinary stood out as the simplest to integrate.

#### Obtaining Cloudinary API and Integrating with Flask

##### 1. Sign Up and Get API Credentials
- **Sign Up** at [Cloudinary](https://cloudinary.com) and verify your email.
- **Log In** to your Cloudinary account.
- **Find Your API Credentials** (Cloud name, API Key, and API Secret) in the dashboard.

##### 2. Install Cloudinary Python SDK
- Run the following command to install:
  ```sh
  pip3 install cloudinary
  ```

#### 3. Add Your Cloudinary API Key to Your `env.py`

    ```python
    os.environ.setdefault("CLOUDINARY_URL", "cloudinary://<api_key>:<api_secret>@<cloud_name>")
    ```

#### 4. Configure Cloudinary in Your Python Application

Use the `CLOUDINARY_URL` stored in your `env.py` file to configure Cloudinary in your Python application.

      ```python
      if os.path.exists("env.py"):
          import env
      app.config["CLOUDINARY_URL"] = os.environ.get("CLOUDINARY_URL")
      ```

#### 5. Configure Cloudinary in Your Python Application

      ```python
      @app.route('/upload', methods=['POST'])
      def upload_file():
        file = request.files["file"]
        result = cloudinary.uploader.upload(file)
        file_url = result['secure_url']
      ```

### Local Deployment
This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the requirements.txt file.

pip3 install -r requirements.txt

You will need to create a new file called env.py at the root-level, and include the same environment variables listed above from the Heroku deployment steps, plus a few extras.

#### Cloning

You can clone the repository by following these steps:

- In the [GitHub repository](https://github.com/pagaslav/theknee-surgery), locate the Code button above the list of files and click it.

- Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard.

- Open Git shell or Terminal.

- Change the current working directory to the one where you want the cloned directory.

- In your IDE Terminal, type the following command to clone my repository:

  - git clone https://github.com/pagaslav/theknee-surgery.git

- Press Enter to create your local clone.

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

- Log in to GitHub and locate the [GitHub repository](https://github.com/pagaslav/theknee-surgery).

- At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.

- Once clicked, you should now have a copy of the original repository in your own GitHub account.

There is no difference between the local version and the deployed version.

## Credits

### Content

#### Terms and Conditions

The Terms and Conditions for this project were sourced from [TermsFeed](https://www.termsfeed.com/), a platform that provides templates and generators for legal documents. These terms were adapted to fit the specific needs of The Knee Surgery website, ensuring that they are relevant to the services provided and the target audience. This addition helps make the project more realistic and professional by outlining the legal guidelines and user responsibilities clearly.

#### Privacy Policy

The Privacy Policy was also generated using [TermsFeed](https://www.termsfeed.com/), ensuring comprehensive coverage of all necessary legal aspects related to user data and privacy. This policy was customized to align with the operations and data handling practices of The Knee Surgery website. Including a Privacy Policy enhances the authenticity of the project, demonstrating a commitment to user privacy and data protection, which is crucial for any real-world website.

### Images

#### Index page

1. Doctor Illustrator Design, [License.](documentation/images/image-1-license-certificate.txt)
2. Physiotherapist check X ray, [License.](documentation/images/image-2-license-certificate.txt)
3. Hands operating a patient, [License.](documentation/images/image-3-license-certificate.txt)
4. Knee joint model , [License.](documentation/images/image-4-license-certificate.txt)
5. Ligament Reconstruction image was generated using AI from [ChatGPT](https://www.openai.com/chatgpt)
6. Bandaging woman's injured knee, [License.](documentation/images/image-6-license-certificate.txt)
7. Injection Procedures, [License.](documentation/images/image-7-license-certificate.txt)

#### Our Doctors page

1. Dr. John Doe photo, [License.](documentation/images/image-8-license-certificate.txt)
2. Dr. Jane Smith photo, [License.](documentation/images/image-9-license-certificate.txt)
3. Dr. Emily Johnson photo, [License.](documentation/images/image-10-license-certificate.txt)
4. Dr. Michael Brown photo, [License.](documentation/images/image-11-license-certificate.txt)

#### About Us page

1. Hospital reception counter, [License.](documentation/images/image-12-license-certificate.txt)
2. Busy Hospital Corridor, [License.](documentation/images/image-13-license-certificate.txt)
3. Modern operating theatre, [License.](documentation/images/image-14-license-certificate.txt)
4. A room of an hospital, [License.](documentation/images/image-15-license-certificate.txt)

## Acknowledgments

- [Code Institute](https://codeinstitute.net/) tutors and Slack community members for their support and help.
  
- [Iuliia Konovalova](https://github.com/IuliiaKonovalova), my mentor, for her invaluable advice and guidance during our online meetings.

- I am deeply grateful for the experience I had nine years ago when I severely injured my knee while skiing. Unable to walk without assistance for almost a year, the doctors' expertise saved my knee. Today, I am able to run, play sports, and even do a bit of jumping. This life-changing experience inspired me to create this website.

- I also want to express my gratitude to my neighbor, a surgeon who specializes in knees and joints. Despite being one of the most remarkable people I've ever known, his practice does not have a website. My project is dedicated to him. After receiving my evaluation, I plan to offer this project to him, adapting it for his clinic. With some enhancements, which I simply did not have time to implement, this website will truly come to life.

- [Stack Overflow](https://stackoverflow.com/): For being an indispensable resource for troubleshooting and problem-solving. The community's expertise and willingness to help have been critical to overcoming many technical challenges.
  
- [Kevin Powell](https://www.youtube.com/user/KepowOb) for his amazing CSS tutorials.
  
- A heartfelt thank you to the creators of [Bootstrap](https://getbootstrap.com/) for providing an excellent style framework. Their toolkit not only accelerates the
development process but also empowers beginners to exceed their own
capabilities.

## Future Improvements

Websites with a backend structure similar to this project offer a wide range of opportunities for continuous improvement and modernization. This ongoing evolution is driven not only by advancing technologies but also by the practical experiences of a real working team. As the team uses the site and gains real-world insights, the site can be further customized and adapted to meet the specific needs of the team and business.

Here are a few key improvements planned for the future:

1. **Enhanced Appointment Management System**
  - Develop a more intuitive appointment management system that simplifies each stage of the process. This includes allowing admins to easily view, edit, and delete appointments as needed. The goal is to make the system as user-friendly and efficient as possible for all users involved.

2. **Addition of Articles and Helpful Materials**
  - Add articles and useful materials to the site that address issues related to the clinic's profile or prepare patients for various procedures. This will provide valuable information and support to patients, enhancing their experience and knowledge.

3. **Search Functionality**
  - Implement a search mechanism for the website. This will enable users to search through articles, doctors to search for patients, and admins to search through all users. This feature will enhance the usability and efficiency of the platform.

4. **Interactive Image**
  - The main page of this project was designed to include an interactive image feature. However, due to time constraints, this feature was not implemented in the current version. I plan to add this interactive element in future updates to enhance the user experience and functionality of the site.

5. **And Much More**
  - Continuously add features and improvements as necessary, based on real-world use and feedback from the team and users. This ongoing development will ensure the platform remains relevant and effective in meeting its users' needs.


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome USER_NAME,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **June 18, 2024**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

### Connecting your Mongo database

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose **mongosh (2.0 or later)** for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- in the terminal, paste the copied code `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --apiVersion 1 --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password _(will not echo **\*\*\*\*** on screen)_

------
