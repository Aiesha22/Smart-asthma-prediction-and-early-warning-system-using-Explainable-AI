import streamlit as st
import sqlite3
import hashlib
from email_utils import send_otp

DATABASE = "asthma.db"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():

    st.title("📝 Register")

    if "generated_otp" not in st.session_state:
        st.session_state.generated_otp = None

    if "otp_sent" not in st.session_state:
        st.session_state.otp_sent = False

    fullname = st.text_input("Full Name")
    email = st.text_input("Email")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")
    otp = st.text_input("Enter OTP")

    clicked = st.button("✅ Register")
    st.write("BUTTON CREATED")

    if clicked:
        st.success("Button works!")

        if password != confirm:
            st.error("Passwords do not match.")
            return

        if not st.session_state.otp_sent:

            st.write("Calling send_otp...")
            generated = send_otp(email)
            st.write("Generated OTP:", generated)

            st.session_state.generated_otp = generated
            st.session_state.otp_sent = True

            st.success("OTP sent to your email.")
            st.info("Click Register again after entering the OTP.")
            return

        if otp != st.session_state.generated_otp:
            st.error("Invalid OTP")
            return

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? OR email=?",
            (username, email)
        )

        user = cursor.fetchone()

        if user:
            st.error("Username or Email already exists.")

        else:
            cursor.execute(
                """
                INSERT INTO users(fullname,email,username,password)
                VALUES(?,?,?,?)
                """,
                (
                    fullname,
                    email,
                    username,
                    hash_password(password)
                )
            )

            conn.commit()

            st.success("Registration Successful!")

            st.session_state.otp_sent = False
            st.session_state.generated_otp = None

        conn.close()