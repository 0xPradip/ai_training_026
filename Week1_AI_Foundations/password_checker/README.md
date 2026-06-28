# 🔐 Password Strength Checker

A simple Password Strength Checker built using **Python** and **Streamlit**. This web application allows users to enter a password and instantly check whether it is **Weak**, **Medium**, or **Strong** based on predefined rules.

## 🚀 Features

- User-friendly web interface with Streamlit
- Hidden password input field
- Password strength classification:
  - 😬 Weak Password
  - 👌 Medium Password
  - 💪 Strong Password
- Fast and lightweight application

## 📋 Password Evaluation Rules

The application checks:

1. Password length (minimum 6 characters)
2. Presence of at least one digit (`0-9`)
3. Presence of at least one uppercase letter (`A-Z`)
4. Presence of at least one special character (`!@#$%^&*`)

### Strength Criteria

| Score | Strength |
|---------|----------|
| 0-1 | Weak 😬 |
| 2 | Medium 👌 |
| 3 | Strong 💪 |

## 🛠️ Technologies Used

- Python 3
- Streamlit

## 📂 Project Structure

```text
password-strength-checker/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/password-strength-checker.git
cd password-strength-checker
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install Streamlit directly:

```bash
pip install streamlit
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

If Streamlit is not recognized:

```bash
python -m streamlit run app.py
```

The application will open automatically in your browser.

## 📸 Demo

Enter a password and click **Check Strength** to see the result.

Example:

| Password | Result |
|-----------|---------|
| abc | Weak |
| abc123 | Weak |
| Abc123 | Medium |
| Abc@123 | Strong |

## 🧠 Core Logic

```python
def check_password(password):
    if len(password) < 6:
        return "Weak Password: Too Short"

    has_digit = any(x.isdigit() for x in password)
    has_upper = any(c.isupper() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)

    score = sum([has_digit, has_upper, has_special])

    if score == 3:
        return "Strong 💪 Password"
    elif score == 2:
        return "Medium 👌 Password"
    else:
        return "Weak 😬 Password"
```

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Submit a Pull Request

## 📄 License

This project is open-source and available under the MIT License.

---

Made with ❤️ using Python and Streamlit.