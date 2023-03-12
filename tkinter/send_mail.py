import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username = "ctxtest@tadiran-group.co.il"
password = "Aa1234"
mail_from = "ctxtest@tadiran-group.co.il"
mail_to = "ddady1@gmail.com"
mail_subject = "Test Subject from Python"
mail_body = "This is a test message"

mimemsg = MIMEMultipart()
mimemsg['From']=mail_from
mimemsg['To']=mail_to
mimemsg['Subject']=mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))
connection = smtplib.SMTP('smtp.office365.com', 587)
connection.starttls()
connection.login(username,password)
connection.send_message(mimemsg)
connection.quit()