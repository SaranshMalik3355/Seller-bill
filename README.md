🛒 Stationery Shop CLI Application

A modular command-line based Stationery Shop Management System built in Python.

This project simulates a small shop system with:

📦 Inventory Management

🧾 Billing System with formatted invoice

🧮 Built-in Calculator

🔒 Safe input handling & validation

💰 ₹ currency formatting

🚀 Features
1️⃣ Inventory Management

Add new items with price

Remove existing items

Input validation for price

Command-based interaction (add, remove, exit)

2️⃣ Billing System

Add multiple products to cart

Accumulates quantity if product entered multiple times

Validates product existence

Validates quantity input

Professionally formatted invoice output

₹ currency formatting

Grand total calculation

Example Output:

---------------------------------------------------------------------------
Product Name           Quantity        Unit Price         Line Total
---------------------------------------------------------------------------
Pen                         2            ₹ 20.00            ₹ 40.00
Register                    1            ₹ 50.00            ₹ 50.00
---------------------------------------------------------------------------
Total Amount                                  ₹ 90.00
---------------------------------------------------------------------------
3️⃣ Calculator Module

Supports:

Addition (+)

Subtraction (-)

Multiplication (*)

Division (/)

Modulo (%)

Includes:

Float support

Zero division protection

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

📂 Project Structure
main()
 ├── inventory_management()
 ├── generate_bill()
 └── calculator()
▶️ How to Run

Make sure Python 3.10+ is installed (for match-case support).

Clone the repository.

Run:

python your_file_name.py
📈 Future Improvements (Planned)

Add stock quantity tracking

Add GST & discount calculation

Add invoice number & timestamp

Save bill to file

Convert to OOP-based design

Refactor repeated input validation into helper functions

🏆 Learning Outcome

This project helped practice:

Structured CLI architecture

Clean control flow

Data accumulation logic

Formatting console output

Proper scope handling

Modular function design
