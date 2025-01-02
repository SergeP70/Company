# install SSL certificate when SSL-error
# /Applications/Python/3.12/Install/Certificates.command with admin privileges
import smtplib
import ssl
from email.message import EmailMessage

host = "smtp.gmail.com"
port = 465
my_context = ssl.create_default_context()
username= "sergepille70@gmail.com"
password = "wooq cdbp lvkf yzpd"

def send(receiver, subject, message):
    mail = EmailMessage()
    mail['From'] = username
    mail['To'] = receiver
    mail['Subject'] = subject
    message = message + "\n This is a message from: " + receiver
    mail.set_content(message)

    # subject = "Subject: Portfolio: Message from " + receiver + "\n\n"
    print(mail)
    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.send_message(mail)
        server.quit()

