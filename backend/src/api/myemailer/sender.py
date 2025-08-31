import os
import smtplib
import ssl
from email.message import EmailMessage

EMAIL_SERVER = os.environ.get("EMAIL_SERVER")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_USERNAME = os.environ.get("EMAIL_USERNAME")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_FROM = os.environ.get("EMAIL_FROM")
EMAIL_TO = os.environ.get("EMAIL_TO")

def send_email(subject: str = "No subject", body: str = "No message body", to_email: str = EMAIL_TO) -> dict:
    message = EmailMessage()
    message["From"] = EMAIL_FROM
    message["To"] = to_email
    message["Subject"] = subject
    message.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(EMAIL_SERVER, EMAIL_PORT, context=context) as smtp:
        smtp.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        return smtp.send_message(message)
    