#  FastAPI Product Portal

A complete web application featuring a **FastAPI** backend with **JWT Authentication** and a dynamic **JavaScript** frontend.

##  Application Logic & Features

### 1. Security & Authentication
The app uses a robust security layer to protect data:
* **Password Hashing:** Uses `bcrypt` via `passlib`. Even if the database is leaked, the actual passwords remain secure.
* **JWT Tokens:** When you log in, the server generates a signed token. This token acts like a temporary "ID card" for the user.
* **Dependency Injection:** Every product-related route is protected by `get_current_active_user`, which checks if the user is logged in before allowing access.


### 2. Data Models
The project uses **Pydantic** to strictly define what a "Product" and a "User" look like:
* **Product:** Requires a `name`, `sku`, `price`, and `url`.
* **Validation:** If you try to send a string where a number (price) belongs, FastAPI will automatically block the request and send a clear error message.

---

##  Test Credentials

| Username | Password | Email |
| :--- | :--- | :--- |
| `john_smith` | `password123` | john_smith@example.com |
| `jane_doe` | `password456` | jane_doe@example.com |

---

## 🛠️ Setup & Execution

1. **Prerequisites:**
   ```bash
   pip install fastapi[all] pyjwt passlib[bcrypt] python-multipart
