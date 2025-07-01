# 🛒 Smart Grocery Billing System

A Python-based console application to manage a grocery store — built to handle product inventory, customer orders, and generate printable bills. Simple, useful, and easy to expand with features like QR payments and GUI.

---

## 💡 Features

### 👤 Owner Module:
- Add new products with quantity and price
- Update existing product details
- View low-stock alerts (products < 10 in quantity)
- Generate and save customer bills
- Load previously saved bills

### 🛍️ Customer Module:
- View all available products
- Place an order (adds items to cart)
- Generate and view bill
- Choose between Cash or QR code payment option

---

## 🔧 Technologies Used

- Python 3
- JSON (for persistent data storage)
- `qrcode` module (for payment QR code)

---

## 🛠️ Installation

1. Clone the repo or download the `.zip`
   ```bash
   git clone https://github.com/<your-username>/Smart-Grocery-Billing.git
