'''
For this project we will be writing a python script to login into 
an email account and send mail using SMPT
'''

import smtplib
from email import encoders
from email.mime.text import MIMEText as mt
from email.mime.base import MIMEBase as mb
from email.mime.multipart import MIMEMultipart as mmp

server = smtplib.SMTP ('smtp.gmail.com', 25) #smtp server and port
server.ehlo()
server.starttls()
server.ehlo()   #to start the service

'''
For our login, it's dangerous to just use clear text as our password.
ex. server.login(mail@mail.com, 'password')

A more secure way to do this would be to save the password encrypted in a txt file,
load the txt and then decrypt

I could also just type in the password everytime i start this, which is slower
'''
with open('password.txt', 'r') as f:
    password = f.read()

server.login('tt1388734@gmail.com', password)

msg = mmp()
msg['From'] = 'Spingy'
msg['To'] = 'hfaiizqunjqfuqflbg@tmmwj.com'

with open('msg.txt', 'r') as f:
    message = f.read()
    
msg.attach(mt(message, 'plain'))

text = msg.as_string()
server.sendmail('tt1388734@gmail.com', 'hfaiizqunjqfuqflbg@tmmwj.com', text)
