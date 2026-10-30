🛍️ ShopEasy – E-Commerce Website

ShopEasy is a beginner-friendly e-commerce web application developed as part of the CodeAlpha Internship. It provides a simple online shopping experience where users can browse products, view product details, manage their shopping cart, and place orders.

The project is built using HTML, CSS, JavaScript, Python, Django, and SQLite.

📌 Project Information
Details	Description
Project Name	ShopEasy
Internship	CodeAlpha
Project Type	E-Commerce Web Application
Frontend	HTML, CSS, JavaScript
Backend	Python, Django
Database	SQLite
Python Version	3.13.15
Django Version	6.1.2
✨ Features
🛒 1. Product Management
Display available products on the homepage.
View individual product details.
Display product name, description, price, image, and available stock.
🛍️ 2. Shopping Cart
Add products to the shopping cart.
Update product quantities.
Remove products from the cart.
Maintain cart contents using Django sessions.
Validate requested quantities against available stock.
👤 3. User Authentication
User registration.
User login and logout.
Display username and account navigation.
Protect customer-specific functionality using Django authentication.
📦 4. Checkout and Orders
Create customer orders from the shopping cart.
Store order details in the database.
Save product names, prices, and quantities in order items.
Track order totals and order status.
Display an order confirmation page.
Allow customers to view their previous orders through the My Orders page.
Note: Checkout, order confirmation, and My Orders functionality should be considered verified only after completing the final testing checklist.
⚙️ 5. Django Admin
Manage products through Django Admin.
View and manage customer orders.
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
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── shop/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_order_orderitem.py
│   │   └── ...
│   │
│   ├── templates/
│   │   └── shop/
│   │       ├── home.html
│   │       ├── product_detail.html
│   │       ├── cart.html
│   │       ├── checkout.html
│   │       ├── order_confirmation.html
│   │       └── my_orders.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── .gitignore
└── README.md


Note: This is an illustrative project structure. Actual files and template names may differ.

🗄️ Database Models

The application uses Django models and SQLite to store product and order information.

1. Product

Stores information about products available for purchase.

Field	Description
name	Product name
description	Product description
price	Product price
image	Product image
stock	Available quantity
created_at	Product creation date
2. Order

Stores customer order information.

Field	Description
customer	Customer who placed the order
created_at	Order creation date
total_amount	Total order amount
status	Current order status
3. OrderItem

Stores products and quantities associated with each order.

Field	Description
order	Related order
product	Related product
product_name	Saved product name
price	Product price at purchase
quantity	Ordered quantity

Database Management: Django migrations are used to manage database schema changes.

🚀 Getting Started

Follow these instructions to run the project on your local machine.

Prerequisites

Make sure the following are installed:

Python 3.13.15 or a compatible Python version.
pip (Python package installer).
Git.
1. Clone the Repository
bash
git clone https://github.com/arunesh-arch/EcommerceProject-CodeAlpha.git


Navigate to the project directory:

bash
cd EcommerceProject-CodeAlpha

2. Create a Virtual Environment
bash
python -m venv venv


Activate the virtual environment.

Windows (Command Prompt):

cmd
venv\Scripts\activate


Windows (PowerShell):

powershell
.\venv\Scripts\Activate.ps1


Linux / macOS:

bash
source venv/bin/activate

3. Install Dependencies

If requirements.txt is available:

bash
pip install -r requirements.txt


If the file is not available, install the dependencies required by the project and create a requirements file before publishing.

4. Apply Database Migrations
bash
python manage.py migrate

5. Run the Development Server
bash
python manage.py runserver


Open your browser and visit:

http://127.0.0.1:8000/

🔐 Django Admin Access

To access the Django Admin dashboard, first create a superuser account:

bash
python manage.py createsuperuser


Follow the instructions to create your administrator credentials.

Start the development server:

bash
python manage.py runserver


Visit the Django Admin page:

http://127.0.0.1:8000/admin/

Log in using your superuser credentials to manage products and inspect orders.

🧪 Testing Checklist

Before submitting the project for internship evaluation, verify the following functionalities.

Homepage and Products
Homepage and product listings load correctly.
Product detail pages display the correct information.
User Authentication
Users can register successfully.
Users can log in and log out.
Shopping Cart
Products can be added to the cart.
Product quantities can be updated.
Products can be removed from the cart.
Cart quantities cannot exceed available stock.
Checkout and Orders
Checkout creates an order with the correct total.
Stock decreases correctly after a successful order.
The cart is cleared after successful checkout.
Checkout rejects an empty cart.
Checkout rejects insufficient stock without creating an invalid order.
Order confirmation displays the correct order information.
Authenticated customers can view their own orders.
Anonymous visitors are redirected to login when accessing My Orders.
Customers cannot access another customer's orders.
Django Admin and Final Checks
Django Admin provides access to Product, Order, and OrderItem.
Existing cart operations continue to work.
python manage.py check completes successfully.
Relevant screenshots are captured for internship submission.
🔒 Security and Configuration Notes
Keep Django's production SECRET_KEY private.
Never upload passwords, API credentials, or other sensitive information.
Add .env files and virtual environments to .gitignore.
Use appropriate access controls for customer-specific order information.
Configure production settings before hosting the website publicly.
Do not use Django's development server for production deployment.
🎯 Project Objectives

The main objectives of ShopEasy are to:

Understand Django web application development.
Implement user authentication and session-based shopping cart functionality.
Work with database models and migrations.
Build a basic order and checkout workflow.
Learn to manage application data through Django Admin.
Practice testing and documenting a full-stack web application.
🔮 Future Improvements

Possible future enhancements include:

Improved responsive design.
Product search and filtering.
Product category navigation.
Better order status display.
Deployment to a hosting platform.

These are optional enhancements and are not required for the current project scope.

👨‍💻 Internship Information

Internship: CodeAlpha
Project: ShopEasy – E-Commerce Website
Developed By: GitHub Profile
Repository: ShopEasy – GitHub

Developed as part of the CodeAlpha Internship to practice full-stack web development using Python and Django.

⭐ If you find this project useful, consider giving the repository a star!


Sample Screenshots:

<img width="773" height="411" alt="Homepage" src="https://github.com/user-attachments/assets/8f49decb-736a-473f-ba0b-5ba5ab310103" />
<img width="771" height="266" alt="Login Page" src="https://github.com/user-attachments/assets/2cc87d7c-ee19-4c10-84a2-56cbc561b1a7" />
<img width="725" height="387" alt="intropage" src="https://github.com/user-attachments/assets/01b4cdbf-3070-45bc-addd-f4cf4cc51045" />
<img width="725" height="387" alt="Checkout page" src="https://github.com/user-attachments/assets/0483e2d9-2057-44b6-9be3-224d4cec8531" />
<img width="561" height="238" alt="Admin page" src="https://github.com/user-attachments/assets/7af7a0f3-a4e0-4241-8899-8cb1b2e2ea5b" /> <img width="743" height="371" alt="Admin Console with Products" src="https://github.com/user-attachments/assets/5a890f6e-0a52-4e6e-82b5-f509b8caf2ef" />
<img width="665" height="287" alt="Products Limits" src="https://github.com/user-attachments/assets/57e4f60f-181a-46c8-bc3c-7790cfeb8cae" />
<img width="743" height="387" alt="Products Page" src="https://github.com/user-attachments/assets/814102b8-e5cf-4c59-aca4-ddf115170848" />




