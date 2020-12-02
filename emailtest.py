import smtplib, ssl
from time import sleep

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "reactenmail@gmail.com"  # Enter your address
receiver_email = "apimpnamedcokemeister@gmail.com"  # Enter receiver address
password = "Strong!Pasword"
message = """\
Subject: Hi there

Don't forget to practice with reacTen and stay active

"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    sleep(30)
