import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
#we could have imported the os library

html=Template(Path('index.html').read_text())
email=EmailMessage()
email['from']='Rohit Papnai'
email['to']='abcd@a.in'
email['subject']='you won a million dollar'
email.set_content(html.substitute({'name':'tin-tin'},'html'))
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dummyemail@gmail.com','password')
    smtp.send_message(email)
    print('all done ')
