import smtplib, ssl
import getpass
import time
port = 465
print("Simple SMTP server")
time.sleep(1)

sender_email = (input(str("Enter your Email Address:\n")))
print("")
time.sleep(1)

receiver_email = (input(str("Enter Receiver Email:\n")))
print("")

sender_password = getpass.getpass(prompt="Enter Your Email Password:\n", stream=None)
message = "file"
print("")
time.sleep(1)
print("[Attempting to Login...]")
try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
        print("Email sent successfully!")
except smtplib.SMTPAuthenticationError:
    print("Something went wrong, try {https://support.google.com/mail/?p=BadCredentials} to adjust your Google Account.")