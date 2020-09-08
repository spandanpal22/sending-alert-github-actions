import os, time, requests
from boltiot import Sms, Email

# later use time to avoid alerts at times you are busy

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandboxcc538641e93641148fe24b216f0e0fec.mailgun.org/messages",
		auth=("api", "41a8c10b9fa6faeedafdfbb6ae7f48c9-52b0ea77-2d3c5097"),
		data={"from": "Excited User <mailgun@sandboxcc538641e93641148fe24b216f0e0fec.mailgun.org>",
			"to": [os.environ['RECIPIENT_EMAIL']],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})

if(os.environ['IS_ACTIVATED']==1):
    response=send_simple_message()
    print("Response EMAIL",response)

    sms = Sms(os.environ['SSID'], os.environ['AUTH_TOKEN'], os.environ['TO_NUMBER'], os.environ['FROM_NUMBER'])
    # mailer = Email(os.environ['MAILGUN_API_KEY'], os.environ['SANDBOX_URL'], os.environ['SENDER_EMAIL'], os.environ['RECIPIENT_EMAIL'])

    response = sms.send_sms("Testing")
    print("Response SMS",response)
    # response = mailer.send_email("Alert", "Testing" )
    # print("Response EMAIL",response)