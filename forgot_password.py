import streamlit as st
import sqlite3
import hashlib
from email_utils import send_otp


DATABASE = "asthma.db"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def forgot_password():

    st.title("🔑 Forgot Password")


    if "reset_otp" not in st.session_state:
        st.session_state.reset_otp = None

    if "reset_email" not in st.session_state:
        st.session_state.reset_email = None



    email = st.text_input("Email")


    # Send OTP

    if st.button("Send Verification Code"):

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()


        cursor.execute(
            "SELECT email FROM users WHERE email=?",
            (email,)
        )


        user = cursor.fetchone()

        conn.close()


        if user is None:

            st.error("Email not found.")

        else:

            otp = send_otp(email)


            st.session_state.reset_otp = otp
            st.session_state.reset_email = email


            st.success(
                "Verification code sent to your email."
            )




    entered_otp = st.text_input(
        "Enter Verification Code"
    )


    new_password = st.text_input(
        "New Password",
        type="password"
    )


    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )



    if st.button("Reset Password"):


        if st.session_state.reset_otp is None:

            st.error(
                "Please request verification code first."
            )

            return



        if entered_otp != str(
            st.session_state.reset_otp
        ):

            st.error(
                "Invalid verification code."
            )

            return



        if new_password != confirm_password:

            st.error(
                "Passwords do not match."
            )

            return



        conn = sqlite3.connect(DATABASE)

        cursor = conn.cursor()


        cursor.execute(
            """
            UPDATE users
            SET password=?
            WHERE email=?
            """,
            (
                hash_password(new_password),
                st.session_state.reset_email
            )
        )


        conn.commit()
        conn.close()



        st.success(
            "Password Updated Successfully!"
        )


        st.session_state.reset_otp = None
        st.session_state.reset_email = None