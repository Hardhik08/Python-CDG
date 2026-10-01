import smtplib
from email.message import EmailMessage

sender_email = "ENTER YOUR EMAIL"
password = "ENTER YOUR APP PASSWORD"
receiver_email = "ENTER RECIPIENT EMAIL"

subject = "Test Email"
body = '''

Hello,

This is a test email sending from a python script

Best Regards,
Your Name

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


