import smtplib
from email.mime.text import MIMEText

import get
from variables import *

# Email credentials
def send():
    msg = MIMEText(get.get())
    msg['From'] = sender_email
    msg['To'] = f'{number}@{carrier}'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, [msg['To']], msg.as_string())
print('SMS sent successfully!')







