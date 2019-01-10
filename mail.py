# Sending mail using Networking
import smtplib
from email.mime.text import MIMEText
from index import headline_filtered

body = ''
for i in headline_filtered:
    body += "'%s\n'" % i
msg = MIMEText(body)
fromaddr = 'noreply.simpleflaskblog@gmail.com'
toaddr = 'amruthavaleveti@gmail.com'
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "cse1234567890")
server.send_message(msg)

# print('Mail sent......')
# server.quit()
