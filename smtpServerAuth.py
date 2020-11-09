import smtplib, ssl
from verseAPI import *
from emailList import *

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#TODO: SETUP EMAIL, FINISH BUILDING EMAIL BODY, SEND TEST EMAIL

sender_email = ""
receiver_email = data
password = input("")

message = MIMEMultipart("alternative")
message["Subject"] = "Daily Bible Verse"
message["From"] = sender_email
message["To"] = receiver_email

text = api_response

html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       Please enjoy this great message.
    </p>
  </body>
</html>
"""


part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)

with smtplib.SMTP_SSL("smtp.mailtrap.io", 2525) as server:
    server.login("04ddca8e7b9429", "d0de88c61bec76")
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )