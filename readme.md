🛍️ ShopEasy — E-Commerce Website

ShopEasy is a beginner-friendly e-commerce web application developed as part of the CodeAlpha Internship. It provides a simple online shopping experience where users can browse products, view product details, manage a shopping cart, and place orders.

The project is built using HTML, CSS, JavaScript, Python, and Django, with SQLite as its database.

📌 Project Information
Project Name: ShopEasy
Internship: CodeAlpha
Project Type: E-Commerce Web Application
Frontend: HTML, CSS, JavaScript
Backend: Python, Django
Database: SQLite
Python Version: 3.13.15
Django Version: 6.1.2
✨ Features
🛒 Product Management
Display products on the homepage.
View individual product details.
Display product information, including name, description, price, image, and available stock.
🛍️ Shopping Cart
Add products to the shopping cart.
Update product quantities.
Remove products from the cart.
Maintain cart contents using Django sessions.
Validate requested quantities against available stock.
👤 User Authentication
User registration.
User login and logout.
Display username and account navigation.
Use authentication to protect customer-specific functionality.
📦 Checkout and Orders
Create customer orders from the shopping cart.
Store order details in the database.
Save product names, prices, and quantities in order items.
Track order totals and order status.
Provide an order confirmation page.
Allow customers to view their previous orders through the My Orders page.

Checkout, order confirmation, and My Orders behavior should be considered verified only after the final testing checklist has passed.

⚙️ Django Admin
Manage products through the Django Admin interface.
View and manage orders.
View associated order items.
🧰 Technologies Used
Technology	Purpose
HTML	Web page structure
CSS	Website styling
JavaScript	Client-side interactions
Python	Backend programming
Django	Web framework
SQLite	Database
Django Templates	Dynamic page rendering
Django Sessions	Shopping cart storage
Django Authentication	User registration and login
Django Admin	Administrative management
📂 Project Structure
text
EcommerceProject/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── shop/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_order_orderitem.py
│   │   └── ...
│   ├── templates/
│   │   └── shop/
│   │       ├── home.html
│   │       ├── product_detail.html
│   │       ├── cart.html
│   │       ├── checkout.html
│   │       ├── order_confirmation.html
│   │       └── my_orders.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── manage.py
├── db.sqlite3
└── README.md


This is an illustrative structure. The actual files and template names may differ in your project.

🗄️ Database Models
Product

Stores information about products available for purchase.

name
description
price
image
stock
created_at
Order

Stores customer order information.

customer
created_at
total_amount
status
OrderItem

Stores the products and quantities associated with each order.

order
product
product_name
price
quantity

The project uses Django migrations to manage database schema changes.

🚀 Getting Started
Prerequisites

Install the following before running the project:

Python 3.13.15, or a compatible Python version.
pip, Python's package installer.
Git, if cloning the project from GitHub.
1. Clone the Repository
bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd EcommerceProject


Replace the placeholder with your actual GitHub repository URL.

2. Create a Virtual Environment
bash
python -m venv venv


Activate it on Windows Command Prompt:

cmd
venv\Scripts\activate

3. Install Dependencies

If a requirements.txt file is included:

bash
pip install -r requirements.txt


If one has not been created, install the project's dependencies according to the existing development environment and create a requirements file before publishing.

4. Apply Database Migrations
bash
python manage.py migrate

5. Run the Development Server
bash
python manage.py runserver


Open the following address in your browser:

http://127.0.0.1:8000/

🔐 Admin Access

Create an administrator account using:

bash
python manage.py createsuperuser


Start the development server and visit:

http://127.0.0.1:8000/admin/

Sign in using your administrator credentials to manage products and inspect orders.

🧪 Testing Checklist

Before submitting the project for internship evaluation, verify the following:

Homepage and product listings load correctly.
Product detail pages display the correct information.
Users can register, log in, and log out.
Products can be added to, updated in, and removed from the cart.
Cart quantities cannot exceed available stock.
Checkout creates an order with the correct total.
Stock decreases correctly after a successful order.
The cart is cleared after successful checkout.
Checkout rejects an empty cart.
Checkout rejects insufficient stock without creating an invalid order.
Order confirmation displays the correct order information.
Authenticated customers can view their own orders.
Anonymous visitors are redirected to login when accessing My Orders.
Customers cannot access another customer's orders.
Django Admin provides access to Product, Order, and OrderItem.
Existing cart operations continue to work.
python manage.py check completes successfully.
Relevant screenshots are captured for the internship submission.
🔒 Security and Configuration Notes
Keep Django's production SECRET_KEY private.
Do not upload passwords, API credentials, or other secrets.
Keep .env files and virtual environments out of version control.
Use appropriate access controls for customer-specific order information.
Use a production-ready deployment configuration before hosting the website publicly.
🎯 Project Objectives

The main objectives of ShopEasy are to:

Understand Django web application development.
Implement user authentication and session-based shopping cart functionality.
Work with database models and migrations.
Build a basic order and checkout workflow.
Learn how to manage application data through Django Admin.
Practice testing and documenting a full-stack web application.
🔮 Future Improvements

Possible future enhancements include:

Improved responsive design.
Product search and filtering.
Product category navigation.
Better order status display.
Deployment to a hosting platform.

These are optional enhancements and are not required for the current project scope.

Internship: CodeAlpha

Project: ShopEasy — E-Commerce Website

GitHub: ](https://github.com/arunesh-arch/EcommerceProject-CodeAlpha.git)

Developed as part of the CodeAlpha Internship to practice full-stack web development using Django.