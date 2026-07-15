import streamlit as st
import sqlite3
import hashlib

DATABASE = "asthma.db"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():

    st.title("📝 Register")

    fullname = st.text_input("Full Name")
    email = st.text_input("Email")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    if st.button("Register"):

        if password != confirm:
            st.error("Passwords do not match.")
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

            st.success("Registration Successful! Please Login.")

        conn.close()