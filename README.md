# inventory_management_system

![GitHub repo size](https://img.shields.io/github/repo-size/KrishnaSreeM/Inventory_Management_System)
![GitHub contributors](https://img.shields.io/github/contributors/KrishnaSreeM/Inventory_Management_System)
![GitHub language count](https://img.shields.io/github/languages/count/KrishnaSreeM/Inventory_Management_System)
![License](https://img.shields.io/github/license/KrishnaSreeM/Inventory_Management_System)

A _web-based Inventory Management System_ built with _Python Flask, **SQLAlchemy, and **Bootstrap_.  
This application allows businesses to efficiently track products across multiple locations, manage stock movements, and maintain a real-time inventory balance.

---

## Table of Contentsp

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Database Structure](#database-structure)
- [Screenshots](#screenshots)
- [Project Architecture](#project-architecture)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- User authentication: Register, login, and logout securely.
- Product management: Add, update, and delete products.
- Location management: Track products in different warehouses or stores.
- Stock movement tracking: Record movement of products between locations.
- Dashboard: View current stock balance and movement history.
- Responsive design: Works well on desktop and mobile devices.

---

## Technologies Used

- _Backend:_ Python, Flask, Flask-Login, SQLAlchemy
- _Frontend:_ HTML, CSS, Bootstrap, JavaScript
- _Database:_ SQLite (can be replaced with MySQL/PostgreSQL)
- _Version Control:_ Git & GitHub

---

## Installation

1. _Clone the repository:_

bash
git clone https://github.com/KrishnaSreeM/Inventory_Management_System.git
cd Inventory_Management_System

2. ## Create a virtual environment and activate it:

bash
python -m venv myenv

# Windows

myenv\Scripts\activate

# macOS/Linux

source myenv/bin/activate

3. ## Install dependencies:

bash
pip install -r requirements.txt

4. ## Run the application

bash
python app.py

5. Open your browser and go to http://127.0.0.1:5000

## Database Structure

- Product: Stores product details (productname, Destricption, etc.).
- Location: Stores warehouse/store information.
- Movement: product name, From to To location, Quanity.
- ProductMovement: Tracks product movements (product, from_location, to_location, quantity).

## Screenshots

### Dashboard

![alt text](<WhatsApp Image 2025-10-05 at 21.48.36_62f96095.jpg>)

### Add Product

![alt text](<WhatsApp Image 2025-10-05 at 21.49.34_00f8183b.jpg>)

## Add Location

![alt text](<WhatsApp Image 2025-10-05 at 21.49.34_e69872b9.jpg>)

## Product Movement

![alt text](<WhatsApp Image 2025-10-05 at 21.49.34_82becbf5.jpg>)

## Report

![alt text](<WhatsApp Image 2025-10-05 at 21.49.35_23694d19.jpg>)

## Contributing

Contributions are welcome!

- Fork the repository
- Create a new branch (git checkout -b feature-name)
- Commit your changes (git commit -m 'Add feature')
- Push to the branch (git push origin feature-name)
- Create a Pull Request

