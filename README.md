# FastShoes

Welcome to FastShoes, your premier online destination for high-quality football footwear designed for athletes. Our modern e-commerce platform features a curated selection of top-notch football shoes, meticulously chosen to enhance your performance on the field.

In addition to our diverse range of shoes available for purchase, we offer convenient features such as the ability to create an account on our website. By creating an account, you can easily add products to your wishlist and write reviews for items you love.

This business idea has always been close to my heart. As a former professional football player, I understand the importance of quality footwear in enhancing performance on the field. FastShoes is my passion project, allowing me to combine my love for football with my desire to learn more about Django and Python.

The live site can be viewed [here](https://fastshoes-be1fd2fa0203.herokuapp.com/)

![Am I responsive screenshot](docs/readme/ami.responsive.png)

## Contents

* [Project Goals](#project-goals)
* [User Experience](#user-experience)
    * [User Stories](#user-stories)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Epics](#epics)
    * [Skeleton](#skeleton)
        * [Wireframes](#wireframes)
        * [Database Schema](#database-schema)
    * [Design Choices](#design-choices)
        * [Typography](#typography)
        * [Colour Palette](#colour-palette)
* [Project Management](#project-management)
* [Features](#features)
    * [Existing Features](#existing-features)
        * [All The Pages](#all-the-pages)
    * [Future Features](#future-features)
* [Technologies Used](#technologies-used)
   * [Languages](#languages)
   * [Frameworks](#frameworks)
   * [Database](#database)
   * [Tools](#tools)
   * [Supporting Libraries and Packages](#supporting-libraries-and-packages)
* [Marketing](#marketing)
* [Testing](#testing)
* [Deployment and Development](#deployment-and-development)
* [Credits](#credits)
* [Acknoledgements](#acknowledgements)

## Project Goals

- I aimed to develop a website equipped with an admin panel for effortless product management and user account handling, seamlessly integrated with a database.

- The objective was to empower admin/staff members to efficiently add, remove, and update products directly from the website while logged in.

- Additionally, I sought to provide admin/staff with the capability to set products on sale to facilitate the clearance of older inventory.

- Users were to be afforded the opportunity to create accounts and manage their account details at their convenience.

- Enhancing user experience, I aimed to implement robust categorization, search, and filtering functionalities to assist users in locating their desired brands with ease.

- To enrich user engagement, I aimed to enable users to curate their own wishlist by adding or removing products, provided they are logged in.

- Furthermore, I aimed to foster user interaction by enabling them to leave reviews for products, enhancing the community aspect of the platform.

- Lastly, I endeavored to provide users with a means to reach out to the FastShoes team through the contact page for any inquiries or assistance needed.

[Back to top](#contents)

## User Experience

### User Stories

The aim of the project was to develop a user-centric website, prioritizing key user stories:

* Store Owner Objectives:
   
   * Craft an engaging design to captivate users
   * Establish a user-friendly front end for intuitive navigation
   * Enable user account management and product management
   * Enable order management

* User Objectives:

   * Enable users to create accounts and retain control over their personal information
   * Deliver a responsive and intuitive design that operates seamlessly across all devices
   * Provide functionality for adding, editing, removing, and updating products in the shopping cart
   * Implement features allowing users to add and remove products from their wishlist, contingent upon user authentication
   * Enable logged-in users to write reviews for products, as well as update or delete their existing reviews as needed.

The objective of e-commerce is to prompt users to explore a variety of products and make purchases. The design is sleek and enables users to categorize and sort products according to their preferences.

Every interaction on the site is meticulously crafted to elicit a positive emotional response from the user. This is achieved through thoughtfully designed information flow, color usage, clear navigation structures, and responsive user action feedback. The absence of intrusive automatic pop-ups ensures a seamless user experience. Users maintain full control over their actions, aided by progress indicators and feedback provided during financial transactions.

### Scope 

Once the structure was established, the focus shifted to the scope phase. This involved defining website requirements aligned with the goals outlined in the strategy phase. These requirements were categorized into two main groups: content and functionality.

Content:

* Privacy Policy has been instituted
* An assortment of purchasable products
* Rating and price of the products
* Information text about each product
* Links to FastShoes social media accounts

Functionality:

* Browse products on the website
* Register and delete accounts as needed
* Easily manage shopping cart items by adding, updating, or removing products
* Save desired products to a personal wishlist for future reference
* Share feedback by leaving reviews for products
* Securely complete orders using Stripe, a trusted payment solution
* Reach out to the store via the contact page for inquiries or assistance
* Stay up-to-date with the latest news, releases, and promotions by subscribing to FastShoes!

### Structure

Navigation:

* Ensure responsive navigation is consistent across all pages for seamless browsing.
* Integrate cart functionality to display the total amount and quantity of products added.
* Implement a search feature enabling customers to easily find products by name, category, or keywords.

Registration and User Profiles:

* Enable user registration and login capabilities for customers to establish and oversee their accounts.
* Implement user authentication and access control mechanisms to guarantee secure and tailored interactions.
* Provide users with the ability to modify their information through the user profile page.
* Allow users to access and monitor their order history via the user profile page.

Products and Sorting:

* Showcase an extensive list of available products.
* Enable users to filter products by category for easier navigation.
* Present comprehensive product details, such as price, images, and ratings.
* Enable users to select their preferred shoe size for the products they desire.

Shopping Cart, Checkout, and Payment Process:

* Users can conveniently add products to their cart and adjust quantities or remove items as needed.
* Ensure a secure checkout process, collecting address and payment details for smooth transactions.
* Integrate a reliable payment gateway, such as Stripe, to facilitate secure online payments.

Admin Panel:

* Develop an intuitive admin panel granting site administrators control over products, categories, wishlists, reviews, contact forms, orders, and user accounts.

Responsive Design:

* Craft a responsive website interface optimized for seamless user experiences across various devices and screen sizes.
* Prioritize intuitive navigation and legible content presentation across desktops, tablets, and mobile devices

Contact Us:

* Integrate a user-friendly contact form or feature to facilitate communication between users and the business.

SEO, Marketing, and Legal:

* Implement a Privacy Policy to ensure compliance with legal regulations.
* Configure robots.txt and sitemap.xml files to facilitate search engine indexing.
* Enhance search engine visibility by optimizing meta descriptions and keywords.
* Establish a Facebook page to promote the business and engage with customers.

### Epics 

In the project planning phase, I started with six main epics and then broke them down into individual user stories. These user stories were labeled and prioritized using the MoSCoW technique (Must have, Should have, Could have, Won't have) to guide their development. This approach helped me concentrate on implementing the most essential features first, ensuring a focused development process. You can view all the user stories on the project board, the link to which is provided below. Additionally, the project board offers a glimpse into upcoming features and developments.

[Project Board For FastShoes](https://github.com/users/balennouri/projects/7)

Below, you'll find the completed user stories for this version of the project, organized by epics:

#### Epic: Initial Django Setup

- As a developer I want to set up Django and install the initial supporting libraries needed so that I can begin development of the site.
- As a developer I want to set up the environment to secure secret configuration variables so that I can ensure sensitive data is kept private.
- As a developer I want to deploy the site to Heroku so that I can ensure the site works in a production environment and share the completed site publicly.

#### Epic: The Website Features

- As a user, I will have it easy to navigate on the page.

- As a user, I will be able to categorize the brand of the products

- As a user, I can filter and search on the website.

- As a user, I can make a wishlist on the website.

- As a user, I want the site to be accessible and user-friendly on mobile devices.

- As a user, I want a seamless experience across different screen sizes.

- As a user, I can write reviews for products.

- As a user, I can contact the store through the contact page

#### Epic: User Authentication and Account Management

- As a first time user, I can create an account

- As a user I can delete my account.

- As a returning user I can login/logout of my account.

- As returning user I can update my profile information.

- As site user I can forget my password and get my account back if so.

- As a user i can add/remove product to the wishlist

- As site owner I can see all the detail information for the users in the admin panel.

#### Epic: Order Management

- As a customer, I want to view my order history.

- As an admin, I want to process and manage customer orders.

#### Epic: Security and Privacy

- As a user, I want my personal and payment information to be secure.

#### Epic: Store Management, Cart and Checkout

- As a admin I can add/delete/update products on the admin panel and on the website.

- As a admin I can add new categories on the admin panel.

- As a user I can rate the product from 0 to 5 in the reviews

- As a user I can add products to the cart.

- As user I can pay directly on the website with my credit card.

- As a user I can update the quantity of the product in the cart and delete the product from the cart.

- As user I can place an order and checkout.

- When a user place a order the cart becomes empty.

### Skeleton

#### Wireframes

I utilized Balsamiq to design my wireframes, creating versions tailored for both larger screens and mobile devices. Wireframing was a crucial step for me to visualize and organize my ideas before diving into the project development. While some pages may deviate slightly from the wireframes, these differences are minor and were made to ensure optimal functionality and user experience during the development process.

##### Home page in wireframe

![wireframe home page](docs/wireframes/home-page-wf.png)

##### Your Profile page in wireframe

![wireframe update profile page](docs/wireframes/my-profile-wf.png)

##### Sign Up page in wireframe

![wireframe sign up page](docs/wireframes/signup-page-wf.png)

##### Login page in wireframe

![wireframe Login page](docs/wireframes/signin-page-wf.png)

##### Products page in wireframe

![wireframe products page](docs/wireframes/products-page-wf.png)

##### Product view page in wireframe

![wireframe product view page](docs/wireframes/view-product-wf.png)

##### Reviews page in wireframe

![wireframe reviews page](docs/wireframes/reviews-page-wf.png)

##### Wishlist page in wireframe

![wireframe wishlist page](docs/wireframes/wishlist-page-wf.png)

##### Shopping cart page in wireframe

![wireframe shopping cart page](docs/wireframes/shopping-cart-wf.png)

##### Place order page in wireframe

![wireframe place order page](docs/wireframes/place-order-wf.png)

#### Database Schema

Below, you'll find the models used in this project. In the database schema displayed below, models with the same color belong to the same app.
The database schema shown here was generated using [FigJam.](https://www.figma.com/)

The Database schema:

![Database schema](docs/readme/datebase.png)

### Design Choices

#### Typography

For the website fonts, I opted to use Kode Mono for the header in the navigation section. For the remaining content, I utilized the Lato font. Additionally, I included a secondary font fallback as Sans-serif to ensure compatibility in case the user's browser does not support the primary fonts. 

#### Colour Palette

![colour pallete](docs/readme/colours.png)

For this website, I opted for darker colors with white used for the content sections. The darker colors complement the colorful nature of football shoes, as most of them feature vibrant colors. This choice ensures that the products stand out effectively when users view them on the website.

The color palette image was generated from [coolers.](https://coolors.co/)

[Back to top](#contents)

## Project Management

I employed agile methodology throughout the project development, utilizing GitHub projects and issues for streamlined management. More detailed information about this approach can be found in the AGILE.md file.

[AGILE.md](https://github.com/balennouri/pp5/blob/main/AGILE.md)

[Back to top](#contents)

## Features

### Existing Features

#### CRUD

The authenticated Store Owner can manage all major product-related functions directly from the front-end of FastShoes. This includes adding new products, editing existing product details, and deleting products entirely, all accessible from either the Products page or the individual Product detail page.

Authenticated users on FastShoes possess significant control over various key functionalities accessible directly from the front-end. They can effortlessly add or remove products from their wishlist, seamlessly manage their account by updating or deleting it, and contribute reviews for all available products on the platform. Furthermore, they retain the ability to edit or delete the reviews they have authored, ensuring a dynamic and personalized user experience.

#### All The Pages

##### The Navigation Bar

![Navbar](docs/readme/features/navbar.png)

##### Admin/Staff: Product Management

![Add Product](docs/readme/features/add-product.png)

![Update Product](docs/readme/features/update-product-page.png)

![Alert Message](docs/readme/features/alert-message-update.png)

##### Home page

![Home Page](docs/readme/features/home-page.png)

##### Product pages

![](docs/readme/features/)

##### User pages

![Contact Us Page](docs/readme/features/contact-us-page.png)

![Sign Up Page](docs/readme/features/sign-up-page.png)

![Login Page](docs/readme/features/login-page.png)

![Profile Page](docs/readme/features/profile-page.png)

![Wishlist Page](docs/readme/features/wishlist-page.png)

##### Shopping Cart/Checkout pages

![Shopping Cart Page](docs/readme/features/shopping-cart.png)

![Checkout Page](docs/readme/features/checkout-page.png)

![Loading Page](docs/readme/features/loading-page.png)

![Order Confirmation](docs/readme/features/order-confirmation-page.png)

![Order message](docs/readme/features/order-success-message.png)

##### The Footer

![Footer](docs/readme/features/footer.png)

### Future Features

Below, you can find my future plans for the website:

* As a user, i can read about the store (About Page)
* As a site user I can add profile image to my account
* As site user I would get a welcome email when I sign up.
* As a customer, I want to track the status of my order.
* As a user I can update the products quantity on the checkout form.
* As a user I can rate the product with stars.
* As a admin/staff the stocks will automatically update when users place an order.

[Back To Top](#contents)

## Technologies Used

<details>

<summary>Click To Expand</summary>

### Languages
* [HTML5](https://html.spec.whatwg.org/)
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
* [JavaScript](https://www.javascript.com/)

### Frameworks

* [Django](https://www.djangoproject.com/)
   * Django was used as the python framework in the project.
* [Bootstrap](https://getbootstrap.com/)
   * The CSS framework that was used for styling the website, saved me a lot of time when I learned to use it.
* [AWS.Amazon](https://us-east-1.console.aws.amazon.com/)
   * I utilized AWS to store both my media and static files for the project.

### Database
 [ElephantSQL](https://www.elephantsql.com/)
   * ElephantSQL serves as the database for the FastShoes project. It is a PostgresSQL database solution that efficiently manages and stores databases.

### Tools
* [Gitpod](https://www.gitpod.io/#get-started)
   * An online integrated development environment (IDE) used for developing and testing the FastShoes project. 
* [GitHub](https://github.com/)
   * A web-based hosting service for version control repositories, used for storing and managing the project's source code.
* [Balsamiq](https://balsamiq.com/wireframes/)
   * A wireframing tool used for creating mockups and prototypes of the FastShoes website.
* [Heroku](https://dashboard.heroku.com/)
   * Used for deploying the page and publish it. Heroku is a cloud platform that enables deployment and hosting of web applications.
* [Stripe](https://stripe.com/).
   * Stripe is a widely used payment processing platform that allows businesses to accept online payments securely.

### Supporting Libraries and Packages

[Back to top](#contents)

</details>

## Marketing

### Marketing Strategies

Subscribing:

* Allow users to subscribe to Fastshoes to receive notifications about new deals and product arrivals, ensuring they stay up-to-date with the latest offerings in the store. By subscribing, users gain exclusive access to promotions and updates, enhancing their shopping experience.

Social Media Marketing - Facebook business page:

![Facebook screenshot](docs/readme/facebook.png)

* Given Facebook's extensive user base and diverse demographic reach, I've established a Facebook Business Page to leverage its marketing potential. Utilizing this platform, I can launch targeted ad campaigns tailored to specific geographic locations, cities, or age groups, maximizing the effectiveness of my marketing efforts. With its widespread popularity and robust advertising features, Facebook presents an ideal platform for promoting my business.

#### SEO

* After incorporating meta tags into the <head> element to enhance my website's visibility and boost its performance on search engines, I proceeded to integrate keywords aimed at attracting both search engines and users. To select the most effective keywords, I utilized [XML-Sitemaps](https://online.seranking.com/login.html) to assess competition and ensure optimal keyword selection. Below, you can find both short-tail and long-tail keywords that were chosen for this purpose.

| Short-Tail | Long-Tail |
|------------|-----------|
| Football Shoes | High-Performance Football Boots for Professional Players
Soccer Cleats | Top Quality Soccer Footwear for Elite Athletes
High-Performance Football Boots | Comfortable Football Boots with Advanced Technology
Top Quality Soccer Footwear | Nike Soccer Cleats for Speed and Agility on the Field
Professional Soccer Cleats | Adidas Soccer Cleats for Precision and Control
Comfortable Football Boots | Puma Soccer Cleats for Dynamic Performance
Nike Soccer Cleats | Professional Soccer Cleats for Serious Players
Adidas Soccer Cleats | Nike Football Boots Engineered for Performance
Puma Soccer Cleats | Adidas Football Boots Designed for Power and Accuracy
Adidas Football Boots | Puma Football Boots for Enhanced Mobility and Comfort
Nike Football Boots | Stylish Nike Soccer Shoes for Athletes
Puma Football Boots | Adidas Soccer Shoes with Cutting-Edge Features
Puma Soccer Shoes | Puma Soccer Shoes for Style and Performance
Nike Soccer Shoes | High-Quality Soccer Cleats for Competitive Matches
Adidas Soccer Shoes | Durable Football Boots for All Playing Conditions

* Furthermore, I employed XML-Sitemaps to generate an XML file. This XML file assists Google in comprehending the website's structure and the interlinking between pages, thereby enhancing the website's search engine optimization (SEO) efforts.

#### Robots.txt and Sitemap.xml

* The robots.txt file, located in the root directory, serves as a directive for search engines, indicating which areas of the application they are not permitted to access. In Bookworms, the robots.txt file includes the URLs of the admin, profile, account, bag and checkout directories, instructing search engine spiders to refrain from crawling these sections.

* The sitemap.xml file, generated on [xml-sitemaps.com](https://www.xml-sitemaps.com/details-mym-bookworms-et-al-b7ea61e35a6e.herokuapp.com-49873d773.html), resides in the root directory and lists essential page URLs of the website. This file assists search engines in comprehending the structure of the website and ensures that all vital pages are crawled and indexed effectively.

#### Privacy Policy

* A Privacy Policy is a document necessary for any online presence that collects data from users. Its purpose is to be transparent and inform users about how their data is being collected and processed. 


[Back To Top](#contents)

## Testing

For the testing part, I conducted manual testing for the entire project. Testing details during and post-development are included in a separate document called [TESTING.md](https://github.com/balennouri/pp5/blob/main/TESTING.md), providing comprehensive insights into the testing process and outcomes. 

Additionally, the document includes :

- Details about manual testing procedures
- Validator test results
- Test results for WAVE, Lighthouse, and various browsers and devices
- Documentation of known bugs and their resolutions

[Testing document link.](https://github.com/balennouri/pp5/blob/main/TESTING.md)

[Back To Top](#contents)

## Deployment and Development

You can access the final deployed site [here](https://fastshoes-be1fd2fa0203.herokuapp.com/). For details about my initial deployment process, please refer to the document named [DEPLOYMENT.md]() included with this repository.

The document covers :

- Setup and Deployment
- The ElephantSQL Database
- Amazon Web Services (AWS)
- Project Settings Adjustments
- Deployment on Heroku
- Forking the Repository
- Cloning The Repository

[Back To Top](#contents)

## Credits

To style the page and the content to Read me : 

- The screenshot at the top of the ReadMe was built from [Ami Responsive.](https://ui.dev/amiresponsive)
- The database schema for the ReadMe was built from [FigJam.](https://www.figma.com/)
- The color palette image was generated from [coolers.](https://coolors.co/)

Insparation Websites :

- [Unisport](https://www.unisportstore.se/)
- [Sportsdirect](https://www.sportsdirect.com/)

To write the code for this project :

- [Code institute LMS](https://learn.codeinstitute.net/dashboard)
- [W3Schools](https://www.w3schools.com/)
- [MDN Web Docs](https://developer.mozilla.org/en-US/)
- [Coding 4 You](http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf)
- [Docs.Djangoproject](https://docs.djangoproject.com/en/5.0/topics/forms/)
- [Docs.Djangoproject](https://docs.djangoproject.com/en/5.0/topics/auth/default/)
- [Django Models Documentation](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django Views Documentation](https://docs.djangoproject.com/en/stable/topics/http/views/)
- [Real Python - Django Models and Databases](https://realpython.com/django-models-databases/)
- [Real Python - Django Views and URLconfs](https://realpython.com/django-views-urlconfs/)
- [DjangoGirls Tutorial](https://tutorial.djangogirls.org/en/)
- [Simple is Better Than Complex - Django Tutorials](https://simpleisbetterthancomplex.com/tutorial/)
- [Medium Django Articles](https://medium.com/tag/django)

Youtube videos that helped me alot :

- [Django Ecommerce Website](https://www.youtube.com/playlist?list=PL-51WBLyFTg0omnamUjL1TCVov7yDTRng)
- [E-commerce FullStack Website using Django](https://www.youtube.com/playlist?list=PL_KegS2ON4s53FNSqgXFdictTzUbGjoO-)
- [Django Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- [YouTube - Django Tutorial for Beginners by Corey Schafer](https://www.youtube.com/watch?v=F5mRW0jo-U4)
- [YouTube - Django Crash Course by Tech With Tim](https://www.youtube.com/watch?v=UmljXZIypDc)

Alternate Projects :

[David Bowers Vape-Store](https://github.com/dnlbowers/Vape-Store)

* For David Bowers' Vape-Store project, I found immense inspiration in its styling, README, and code structure. Utilizing this project as a reference, I benefited from its clean design and usability. Additionally, having David as my mentor allowed me to seek guidance whenever I encountered challenges during development.

[Boutique Ado](https://github.com/mkthewlis/boutique-ado)

* The Boutique Ado project played a pivotal role in my learning journey, offering invaluable inspiration and guidance. I drew extensively from its concepts and methodologies, shaping many aspects of my own project. Those acquainted with Boutique Ado may notice parallels in my work, reflecting its profound impact on my development.

[Back to top](#contents)

## Acknowledgements

* This website serves as my Fifth portfolio project for the Code Institute course in Full Stack Software Development.

* I express my deepest gratitude to my mentor, David Bowers, whose expertise and unwavering support have been instrumental in my journey. His insightful feedback and dedication to improvement have been invaluable.

* I also want to extend my appreciation to the supportive Slack community and the Code Institute team for their guidance and assistance throughout this endeavor.

[Back to top](#contents)