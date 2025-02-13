import sched
import smtplib
import time
from email.mime.text import MIMEText
import schedule
from special_vars import *
import requests

def send():
    msg = MIMEText(requests.get("https://api.ipify.org").text)
    msg['From'] = sender_email
    msg['To'] = 'kadlecekemma@gmail.com'
    msg['Subject'] = "IP"

    total = "YOUR LOCAL IP IS: " + msg.as_string()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, [msg['To']], total)


schedule.every(1).day.at_time(time(hour=5))

while True:
    schedule.run_pending()
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("THING STOPPED OH NOES")
