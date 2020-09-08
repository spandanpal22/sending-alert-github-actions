import os, time
from boltiot import Sms, Email

# print(os.environ['HOME'])

sms = Sms(os.environ['SSID'], os.environ['AUTH_TOKEN'], os.environ['TO_NUMBER'], os.environ['FROM_NUMBER'])
mailer = Email(os.environ['MAILGUN_API_KEY'], os.environ['SANDBOX_URL'], os.environ['SENDER_EMAIL'], os.environ['RECIPIENT_EMAIL'])

# later use time to avoid alerts at times you are busy

response = sms.send_sms("Testing")
print("Response SMS",response)
response = mailer.send_email("Alert", "Testing" )
print("Response EMAIL",response)