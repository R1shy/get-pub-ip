import smtplib
import time
from email.mime.text import MIMEText
import dotenv
except ModuleNotFoundError:
    print("Please make a special special_vars.py file")
    exit(1)
import requests

def send():
    msg = MIMEText(requests.get("https://api.ipify.org").text)
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "IP"

    total = "YOUR LOCAL IP IS: " + msg.as_string()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, [msg['To']], total)



while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("THING STOPPED OH NOES")
        exit(0)
