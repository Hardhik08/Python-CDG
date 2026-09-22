import smtplib
from email.message import EmailMessage

sender_email = "hardhik385@gmail.com"
password = 'rtwl rkfz zikd ktak'
receiver_email = 'pavank9k@gmail.com'

subject = "Test Email"
body = '''

Hi Daddy,

This is a test email sending from a python script

Best Regards,
Hardhik

'''

msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email
msg.set_content(body)

try:
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(sender_email,password)
        smtp.send_message(msg)
        print("Sent Successfully!")

except Exception as e:
    print("Error is", e)


