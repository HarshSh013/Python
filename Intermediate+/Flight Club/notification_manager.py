import smtplib
from twilio.rest import Client

TWILIO_SID = "ACee72c4a3c7b75936ceabdb63da7ed69f"
TWILIO_AUTH_TOKEN = "b1d9d1b02f42d8d22d534e83d237f2d3"
TWILIO_VIRTUAL_NUMBER = +18788812643
TWILIO_VERIFIED_NUMBER = +917073396759
# MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "sharmaeater1@gmail.com"
MY_PASSWORD = "eljznatvitfzlniv"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )