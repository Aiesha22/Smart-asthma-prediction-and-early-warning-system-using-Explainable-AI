import random
import yagmail

EMAIL = "smartasthma102@gmail.com"
PASSWORD = "pqdi juie xxno eiqt"

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp(receiver_email):
    otp = generate_otp()

    yag = yagmail.SMTP(EMAIL, PASSWORD)

    yag.send(
        to=receiver_email,
        subject="Smart Asthma Prediction System",
        contents=f"""
Hello,

Your verification OTP is:

{otp}

Please enter this OTP to complete your registration.

Thank you.
"""
    )

    return otp
