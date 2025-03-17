Key Features of the RIMS Project:
✅ Purchase Entry Management – Records and tracks supplier purchases efficiently.
✅ Sales Entry Module – Captures sales transactions and updates stock in real time.
✅ Stock Requisition System – Manages stock requests and ensures inventory optimization.
✅ Database Integration – Maintains seamless data flow across all modules.
✅ User-Friendly Interface – Designed with UX/UI principles for easy navigation.

RIMS (Retail Inventory Management System)

Overview

RIMS is a web-based application designed to streamline retail operations by managing purchase entry, sales entry, and stock requisition efficiently. The system ensures real-time updates, accurate inventory tracking, and a user-friendly experience.

Features

Purchase Entry: Track and manage supplier purchases.

Sales Entry: Record and monitor sales transactions.

Stock Requisition: Request and manage stock efficiently.

Real-time Database Integration: Ensures accurate data synchronization.

User-friendly UI: Built with HTML, CSS, and JavaScript for seamless interaction.

Technologies Used

Backend: Python (Django Framework)

Frontend: HTML, CSS, JavaScript

Database: MySQL

Installation & Setup

Prerequisites

Ensure you have the following installed:

Python (>= 3.x)

Django (latest version)

MySQL Server

Node.js (for frontend package management, if needed)

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐


Steps to Set Up

1. Clone the Repository:

git clone https://github.com/your-username/RIMS.git
cd RIMS

2. Set Up a Virtual Environment (Optional but Recommended):

python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

3. Install Dependencies:

pip install -r requirements.txt

4. Configure the Database:

Update settings.py with your MySQL credentials.

5. Run migrations:

python manage.py makemigrations
python manage.py migrate

6. Run the Development Server:

python manage.py runserver

7. Access the Application:
Open http://127.0.0.1:8000/ in your browser.

Usage

Admin Panel: Accessible at /admin for managing inventory and transactions.

Purchase & Sales Entry: Navigate through the UI to log purchases and sales.

Stock Requisition: Request stock as needed through the system.
