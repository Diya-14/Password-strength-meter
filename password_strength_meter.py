import streamlit as st
import re
import random
import string
import time
from streamlit_extras.let_it_rain import rain

# # Function to estimate password cracking time
def estimate_crack_time(password):
    char_sets = 0
    if re.search(r"[a-z]", password):
        char_sets += 26
    if re.search(r"[A-Z]", password):
        char_sets += 26
    if re.search(r"\d", password):
        char_sets += 10
    if re.search(r"[!@#$%^&*]", password):
        char_sets += 8
    
    total_combinations = char_sets ** len(password)
    crack_time_seconds = total_combinations / 1000000000  # Assuming 1 billion guesses per second
    if crack_time_seconds < 60:
        return "⏳ Less than a minute"
    elif crack_time_seconds < 3600:
        return "⏳ A few minutes"
    elif crack_time_seconds < 86400:
        return "⏳ A few hours"
    elif crack_time_seconds < 31536000:
        return "⏳ A few days"
    else:
        return "🛡️ Billions of years! Highly Secure!"

# # Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
#     # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    crack_time = estimate_crack_time(password)
    
#     # Strength Rating
    if score >= 4:
        return "✅ Strong Password!🔥", feedback, crack_time
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", feedback, crack_time
    else:
        return "❌ Weak Password - Improve it using the suggestions above.", feedback, crack_time

# # Function to generate a strong password
def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(14))

# # Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="wide")

st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            color: white;
            text-align: center;
            font-family: Arial, sans-serif;
        }
        .stTextInput > div > div > input {
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
            border: 2px solid #fff;
            background: rgba(255, 255, 255, 0.2);
            color: black;
            text-align: center;
            font-weight: bold;
        }
        .stButton > button {
            background: linear-gradient(to right, #ff6b6b, #ff4757);
            color: white;
            padding: 12px 25px;
            font-size: 18px;
            border-radius: 10px;
            border: none;
            transition: 0.3s;
            box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
        }
        .stButton > button:hover {
            transform: scale(1.1);
            background: linear-gradient(to right, #ff4757, #ff6b6b);
        }
        .password-box {
            background: rgba(255, 255, 255, 0.3);
            padding: 25px;
            border-radius: 15px;
            margin-top: 20px;
            box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
        }
        .security-tips {
            font-size: 14px;
            color: #fff;
            margin-top: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔐 Password Strength Meter")
# Captions & Descriptions
st.markdown("<h3>Use strong passwords to stay safe!💻</h3>", unsafe_allow_html=True)
st.markdown("<p style='font-size:21px;'>This tool helps you check your password strength and generates strong passwords to keep your accounts secure. Weak passwords are easy to hack, so always use a combination of letters, numbers, and special characters!</p>", unsafe_allow_html=True)
st.markdown("Ensure your password is strong and secure!")
st.write("Secure your online presence by using strong passwords. This tool helps you check your password strength and generates strong passwords for you!")

password = st.text_input("Enter your password", type="password")

st.markdown("""
     <style>
         body { background-color: #1E1E1E; color: white; text-align: center; font-family: Arial, sans-serif; }
        .stTextInput > div > div > input { border-radius: 10px; padding: 10px; font-size: 16px; text-align: center; }
        .password-box { background: rgba(255, 255, 255, 0.3); padding: 25px; border-radius: 15px; }
    </style>
 """, unsafe_allow_html=True)

if st.button("Check Strength"):
    strength, feedback, crack_time = check_password_strength(password)
    st.markdown(f"### {strength}")
    for fb in feedback:
        st.write(fb)
    st.write(f"⏳ Estimated time to crack: {crack_time}")
    st.markdown("<div class='security-tips'>🔹 Tip: Use a mix of uppercase, lowercase, numbers, and symbols for better security.</div>", unsafe_allow_html=True)
# # Animated Rain Effect
rain(
    emoji="🔑",
    font_size=15,
    falling_speed=5,
    animation_length="infinite"
)
if st.button("Generate Strong Password"):
    strong_password = generate_password()
    st.success(f"🔑 Suggested Strong Password: `{strong_password}`")
    st.write("🔒 Save this password securely!")

