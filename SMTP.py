import smtplib, ssl
import getpass
import time
port = 465
sender_email = (input(str("Enter your Email:\n")))
print("")
time.sleep(2)
receiver_email = (input(str("Enter Receiver Email:\n")))
print("")
context = ssl.create_default_context()
sender_password = getpass.getpass(prompt="Enter Your Email Password:\n", stream=None)
message = "file"
print("")
time.sleep(2)
print("[Attempting to Login...]")
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
except smtplib.SMTPAuthenticationError:
    print("Something went wrong, try {https://support.google.com/mail/?p=BadCredentials} to adjust your Google Account.")