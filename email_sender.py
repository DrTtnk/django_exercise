import os
import smtplib
from email.message import EmailMessage

SMTP_SERVER = os.environ.get('SMTP_SERVER', 'localhost:1025')
EMAIL_ADDRESS = os.environ.get('EMAIL_USER', 'sadafa@gmail.com')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

msg = EmailMessage()
msg['Subject'] = 'Periodic Recap'
msg['From'] = EMAIL_ADDRESS


def send_recap():
    with smtplib.SMTP(SMTP_SERVER) as smtp:
        if 'localhost' not in SMTP_SERVER:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        msg['To'] = 'sadafa@gmail.com'
        msg.set_content('This is a periodic Recap')

        smtp.send_message(msg)


send_recap()
