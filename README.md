🛒 Stationery Shop CLI Application

A modular command-line based Stationery Shop Management System built in Python.

This project simulates a small shop system with:

📦 Inventory Management

🧾 Billing System with formatted invoice

🧮 Built-in Calculator

🔒 Safe input handling & validation

💰 ₹ currency formatting

🚀 Features
📦 Inventory Management

Add new items with price

Remove existing items

Input validation for price

Command-based interaction (add, remove, exit)

Prevents invalid inputs

🧾 Billing System

Add multiple products to cart

Accumulates quantity if product entered multiple times

Validates product existence

Validates quantity input

Professionally formatted invoice output

₹ currency formatting

Grand total calculation

Example Invoice Output
---------------------------------------------------------------------------
Product Name           Quantity        Unit Price         Line Total
---------------------------------------------------------------------------
Pen                         2            ₹ 20.00            ₹ 40.00
Register                    1            ₹ 50.00            ₹ 50.00
---------------------------------------------------------------------------
Total Amount                                  ₹ 90.00
---------------------------------------------------------------------------
🧮 Calculator Module

Supports:

Addition (+)

Subtraction (-)

Multiplication (*)

Division (/)

Modulo (%)

Includes:

Float support

Division-by-zero protection

Modulo-by-zero protection

Safe number validation

Exit-based control

🧠 Design Principles Used

Separation of Concerns

Single Responsibility Principle

Modular Design

Defensive Programming

Input Validation & Error Handling

Each module operates independently and returns cleanly to the main controller.

🏗 Project Structure
main()
 ├── inventory_management()
 ├── generate_bill()
 └── calculator()
▶️ How to Run
Requirements

Python 3.10 or above (required for match-case)

Steps

Clone the repository:

git clone https://github.com/your-username/your-repo-name.git

Navigate to the project folder:

cd your-repo-name

Run the program:

python filename.py
📈 Future Improvements

Add stock quantity tracking

Add GST & discount calculation

Add invoice number & timestamp

Save bill to file

Convert to OOP-based design

Refactor repeated input validation into reusable helper functions

🎯 Learning Outcomes

This project demonstrates:

Structured CLI architecture

Clean control flow

Data accumulation logic

Console output formatting

Proper scope handling

Modular function design

👨‍💻 Author

Developed as a hands-on practice project to strengthen Python fundamentals and system design thinking. 
