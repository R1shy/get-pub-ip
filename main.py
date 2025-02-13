import DateTime
import sched
import smtplib
import time
from email.mime.text import MIMEText

import schedule

from get import *
from variables import *

def send():
    msg = MIMEText(get())
    msg['From'] = sender_email
    msg['To'] = 'kadlecekemma@gmail.com'
    msg['Subject'] = "IP"

    total = "YOUR LOCAL IP IS: " + msg.as_string()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, [msg['To']], total)


schedule.every(1).minutes.do(send)

while True:
    schedule.run_pending()
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("THING STOPPED OH NOES")
