import streamlit as st
import sqlite3
import hashlib
from register import register
from forgot_password import forgot_password
from PIL import Image

DATABASE = "asthma.db"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login():

    logo = Image.open("assets/logo.png")

    st.image(
    logo,
    width=150
)

    choice = st.sidebar.selectbox(
        "Select",
        ["Login", "Register", "Forgot Password"]
    )

    if choice == "Register":
        register()

    elif choice == "Forgot Password":
        forgot_password()

    else:

        st.title("🔐 Smart Asthma Prediction System")

        username = st.text_input("Username")
        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT * FROM users
                WHERE username=? AND password=?
                """,
                (
                    username,
                    hash_password(password)
                )
            )

            user = cursor.fetchone()

            conn.close()

            if user:

                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.session_state["role"] = user[5]

                st.success("Login Successful!")
                st.rerun()

            else:
                st.error("Invalid Username or Password")