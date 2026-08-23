# 🛒 ShopEase – Full-Stack E-Commerce Website

A modern and responsive **full-stack e-commerce web application** built using **React.js, Django, Python, and SQLite**. ShopEase provides a complete online shopping experience with product browsing, user authentication, shopping cart management, and order processing.

## 🚀 Features

* 🏠 Responsive e-commerce homepage
* 🛍️ Product listing and product details
* 🔎 Product browsing by category
* 👤 User registration and login
* 🛒 Add products to shopping cart
* ➕ Increase/decrease product quantities
* ❌ Remove products from cart
* 💰 Automatic cart total calculation
* 📦 Order creation and processing
* 🗄️ Product, user, and order database management
* 🔐 Django-based backend API
* 📱 Responsive design for different screen sizes
* 🖼️ Product images using image URLs
* ⚡ React-based interactive frontend

## 🛠️ Technologies Used

### Frontend

* **React.js**
* **JavaScript**
* **HTML5**
* **CSS3**
* **Axios**
* **Vite**

### Backend

* **Python**
* **Django**
* **Django REST Framework**

### Database

* **SQLite**

### Development Tools

* **Visual Studio Code**
* **Git**
* **GitHub**

## 📂 Project Structure

```text
ShopEase/
│
├── frontend/
│   ├── public/
│   │
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.jsx
│   │   │   ├── ProductCard.jsx
│   │   │   └── ...
│   │   │
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── Cart.jsx
│   │   │   ├── ProductDetails.jsx
│   │   │   └── ...
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── context/
│   │   │   └── CartContext.jsx
│   │   │
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── backend/
│   ├── ecommerce/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   │
│   ├── store/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── management/
│   │       └── commands/
│   │           └── seed_products.py
│   │
│   ├── manage.py
│   └── db.sqlite3
│
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ShopEase.git
cd ShopEase
```

### 2. Set Up the Django Backend

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install django djangorestframework django-cors-headers
```

### 3. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Add Sample Products

The project includes a Django management command for adding sample products:

```bash
python manage.py seed_products
```

This automatically adds **30 products** to the database.

### 5. Create an Admin Account

```bash
python manage.py createsuperuser
```

Follow the instructions to create your administrator account.

### 6. Start the Django Server

```bash
python manage.py runserver
```

The backend will run at:

```text
http://127.0.0.1:8000/
```

The Django administration panel is available at:

```text
http://127.0.0.1:8000/admin/
```

---

## 💻 Frontend Setup

Open another terminal and navigate to the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the React development server:

```bash
npm run dev
```

Vite will provide a local URL, for example:

```text
http://localhost:5175/
```

Open that URL in your browser.

---

## 🔄 Application Workflow

```text
             ┌────────────────────┐
             │     React.js       │
             │     Frontend       │
             └─────────┬──────────┘
                       │
                       │ Axios / REST API
                       ▼
             ┌────────────────────┐
             │      Django        │
             │    REST API        │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │      SQLite        │
             │     Database       │
             └────────────────────┘
```

Users can browse products through the React interface, add products to their cart, authenticate through the Django backend, and place orders. Django manages the application data and database operations.

## 🗄️ Database Models

The backend contains database models for managing:

### Product

Stores:

* Product name
* Description
* Price
* Category
* Image URL
* Stock
* Creation date
* Updated date

### User

Handles:

* Username
* Email
* Password
* Authentication

### Order

Handles:

* Customer
* Ordered products
* Quantity
* Total price
* Order status
* Order date

## 🔌 API Structure

Example API endpoints include:

```text
GET  /api/products/
GET  /api/products/<id>/

POST /api/auth/register/
POST /api/auth/login/

GET  /api/orders/
POST /api/orders/create/
```

The React frontend communicates with these Django REST API endpoints using Axios.

## 🛒 Shopping Cart

The shopping cart allows users to:

* Add products
* Remove products
* Increase quantity
* Decrease quantity
* View individual product prices
* Calculate the total amount
* Proceed toward checkout

## 👨‍💼 Django Admin

Administrators can manage the store through Django Admin.

```text
http://127.0.0.1:8000/admin/
```

The admin interface can be used to:

* Add products
* Edit products
* Delete products
* Manage stock
* Manage users
* View orders

## 🎯 Project Objectives

The main objective of ShopEase is to demonstrate the development of a **full-stack e-commerce application** by integrating a modern React frontend with a Django REST backend and relational database.

The project demonstrates practical knowledge of:

* Frontend development
* Backend development
* REST API integration
* Database management
* Authentication
* CRUD operations
* State management
* E-commerce workflows
* Responsive web design

## 🔮 Future Enhancements

Possible future improvements include:

* 💳 Online payment gateway
* ❤️ Wishlist functionality
* 🔍 Advanced product search
* ⭐ Product reviews and ratings
* 📧 Order confirmation emails
* 📱 Mobile application
* 📊 Admin sales dashboard
* 🔔 Order notifications
* 📦 Order tracking
* 🌙 Dark mode
* 🧾 Downloadable invoices

## 👨‍💻 Author

**Vijith Juvviguntla**

This project was developed as a full-stack web development project to demonstrate practical implementation of **React.js, Django, REST APIs, and database management**.

## 📄 License

This project is intended for **educational and learning purposes**.
