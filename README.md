# 🛒 Stationery Shop CLI Application

> A modular command-line based **Stationery Shop Management System** built in Python — simulating a small shop with inventory control, billing, and a built-in calculator.

---

## ✨ Overview

This project is a hands-on Python CLI application structured around clean, modular design. It covers three core subsystems:

- 📦 **Inventory Management** — Add/remove items with validation
- 🧾 **Billing System** — Cart, invoice generation, and ₹ currency formatting
- 🧮 **Calculator** — Arithmetic operations with safe error handling

---

## 🚀 Features

### 📦 Inventory Management

- Add new items with name and price
- Remove existing items by name
- Input validation for price (no negatives or non-numeric values)
- Command-based interaction: `add`, `remove`, `exit`
- Prevents invalid or duplicate inputs

### 🧾 Billing System

- Add multiple products to a cart
- Accumulates quantity if the same product is entered more than once
- Validates product existence before adding to cart
- Validates quantity input (positive integers only)
- Professionally formatted invoice output with ₹ currency
- Grand total calculation

**Example Invoice Output:**

```
---------------------------------------------------------------------------
Product Name           Quantity        Unit Price         Line Total
---------------------------------------------------------------------------
Pen                         2            ₹ 20.00            ₹ 40.00
Register                    1            ₹ 50.00            ₹ 50.00
---------------------------------------------------------------------------
Total Amount                                  ₹ 90.00
---------------------------------------------------------------------------
```

### 🧮 Calculator Module

Supports the following operations:

| Operation      | Symbol |
|----------------|--------|
| Addition       | `+`    |
| Subtraction    | `-`    |
| Multiplication | `*`    |
| Division       | `/`    |
| Modulo         | `%`    |

Safety features:
- Float number support
- Division-by-zero protection
- Modulo-by-zero protection
- Safe number input validation
- Exit-based control flow

---

## 🧠 Design Principles

| Principle                    | Description                                              |
|-----------------------------|----------------------------------------------------------|
| Separation of Concerns       | Each module handles one domain independently             |
| Single Responsibility        | Each function does exactly one thing                     |
| Modular Design               | Modules return cleanly to the main controller            |
| Defensive Programming        | All inputs are validated before processing               |
| Input Validation             | Clear error messages guide the user on invalid entries   |

---

## 🏗 Project Structure

```
main()
 ├── inventory_management()
 ├── generate_bill()
 └── calculator()
```

---

## ▶️ How to Run

### Requirements

- **Python 3.10+** (required for `match-case` syntax)

### Steps

1. **Clone the repository:**

```bash
git clone https://github.com/SaranshMalik3355/your-repo-name.git
```

2. **Navigate to the project folder:**

```bash
cd your-repo-name
```

3. **Run the application:**

```bash
python main.py
```

---

## 📈 Future Improvements

- [ ] Add stock quantity tracking per item
- [ ] Add GST & discount calculation
- [ ] Add invoice number & timestamp generation
- [ ] Save bill output to a `.txt` or `.pdf` file
- [ ] Convert to an OOP-based design (classes for `Inventory`, `Cart`, `Invoice`)
- [ ] Refactor repeated input validation into reusable helper functions

---

## 🎯 Learning Outcomes

This project demonstrates:

- Structured CLI architecture with a central controller
- Clean control flow using functions and return values
- Data accumulation logic (cart quantity merging)
- Console output formatting (aligned columns, separators)
- Proper variable scoping across modules
- Modular function design with clear responsibilities

---

## 👨‍💻 Author

**Saransh Malik**

Developed as a hands-on practice project to strengthen Python fundamentals and system design thinking.

- 🐙 GitHub: [@SaranshMalik3355](https://github.com/SaranshMalik3355)

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

```
MIT License

Copyright (c) 2025 Saransh Malik

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<p align="center">Made with ❤️ and Python 🐍</p>
