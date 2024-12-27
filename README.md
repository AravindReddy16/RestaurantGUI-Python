# Restaurant Management System GUI

This project implements a simple Restaurant Management System using Python's tkinter library for the graphical user interface (GUI). It allows two types of users:

Admin: To manage the menu by adding or removing items.

Customer: To view the menu, place orders, and checkout.

# Features

# Admin:

Login functionality with default credentials (admin/admin).

Add menu items with a recipe name and price.

Delete menu items by recipe name.

View the complete list of menu items.

# Customer:

Login functionality with default credentials (customer/customer).

View the available menu items.

Add items to the order.

View the total bill for the order.

Checkout and clear the order list.

# Prerequisites

Python 3.x

tkinter library (included with standard Python installations)

# How to Run

Clone or download the repository to your local machine.

Navigate to the project directory.

Run the Python file:

python restaurant_management_gui.py

Use the GUI to interact as an admin or customer.

# Default Credentials

# Admin Login:

Username: admin

Password: admin

# Customer Login:

Username: customer

Password: customer

# Screenshots

# Main Menu

Provides options for Admin or Customer login.

# Admin Dashboard

Options to add, delete, and view menu items.

# Customer Dashboard

Menu display with options to add items to the order, view the bill, and checkout.

# Code Structure

# Classes:

Restaurant: Holds the restaurant name.

# Admin: Manages menu items.

# Customer: Handles customer orders and bill generation.

# RestaurantApp: Implements the GUI using tkinter and integrates Admin and Customer functionalities.

# Key Methods:

# Admin:

login(username, password)

add_item(recipe, price)

delete_item(recipe)

# Customer:

login(username, password)

add_order(item)

calculate_bill()

checkout()

# Contribution

Feel free to fork the repository and submit pull requests for any enhancements or bug fixes. Suggestions and feedback are welcome.
