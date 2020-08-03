import smtplib#for dealing with emails
from email.mime.text import MIMEText # to build the message including the body,subject ,from, to etc.



body="""Hi!
 This is ABC.
 This is a Test Mail."""

msg=MIMEText(body)

msg['From']='From Address@gmail.com'

msg['To']='ToAdress@gmail.com'
msg['Subject']='Hello'

server=smtplib.SMTP('smtp.gmail.com',587)

server.starttls()
server.login('FromAdress@gmail.com','Password')
'''

if you get this error 
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials d13sm2099769pjs.44 - gsmtp')

then login into your account and go to the link below and provide access

https://www.google.com/settings/security/lesssecureapps

Still not working? If you still get the SMTPAuthenticationError but now the code is 534, its because the location is unknown. Follow this link:

https://accounts.google.com/DisplayUnlockCaptcha


Log in to your Google account, and use these links:
Step 1 [Link of Disabling 2-step verification]:

https://myaccount.google.com/security?utm_source=OGB&utm_medium=act#signin

Step 2: [Link for Allowing less secure apps]

https://myaccount.google.com/u/1/lesssecureapps?pli=1&pageId=none

even if not working

https://myaccount.google.com/apppasswords?utm_source=google-account&utm_medium=web


Any How i could not send a mail from my python But Hope these solutions will Help 
'''
server.send_message(msg)

print("Mail Sent")
server.quit()