import streamlit as st
from zxcvbn import zxcvbn

def check_password_strength(password):
    result = zxcvbn(password)
    score = result['score']  # Score ranges from 0 (Weak) to 4 (Strong)
    feedback = result['feedback']['suggestions']
    
    if score == 0:
        strength = "Very Weak"
        color = "#ff4d4d"
    elif score == 1:
        strength = "Weak"
        color = "#ff9966"
    elif score == 2:
        strength = "Medium"
        color = "#ffcc00"
    elif score == 3:
        strength = "Strong"
        color = "#99cc33"
    else:
        strength = "Very Strong"
        color = "#33cc33"
    
    return strength, color, feedback

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", layout="centered")
st.title("🔒 Password Strength Meter")
st.write("Check the strength of your password in real-time!")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, color, feedback = check_password_strength(password)
    
    st.markdown(f"<h3 style='color: {color};'>Password Strength: {strength}</h3>", unsafe_allow_html=True)
    
    if feedback:
        st.warning("Suggestions:")
        for suggestion in feedback:
            st.write(f"- {suggestion}")
