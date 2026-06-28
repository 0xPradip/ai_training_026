import streamlit as st

# Function to check password strength
def check_password(password):
    """Rate password strength: weak/medium/strong"""

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


# Streamlit UI
st.title("🔐 Password Strength Checker")

st.write("Enter a password below to check its strength.")

password = st.text_input(
    "Enter Password",
    type="password",
    placeholder="Type your password here..."
)

if st.button("Check Strength"):
    if password:
        result = check_password(password)

        if "Strong" in result:
            st.success(result)
        elif "Medium" in result:
            st.warning(result)
        else:
            st.error(result)
    else:
        st.warning("Please enter a password.")