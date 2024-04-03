# Gmail Email Sender
# Author: Sissi Zhang

import os
from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'example_email@gmail.com'
email_password = 'password you set up'
# notice: you'll have to turn on 2-step verification of your gmail, and go to
# https://myaccount.google.com/apppasswords
# to set up a 16-character password 

# there is also a website showing the steps: 
# https://support.google.com/mail/answer/185833?hl=en


subject = "Example Email Headline"
body = '''
<p style="font-size: 16px; font-family: Cambria">
Dear {name},
<br><br>

Thank you for reading into my codes! This sample body will serve as a brief introduction 
of how you should write the body of your customized email!
<br><br>

Basically, the line-breaks inside python will not be recognized or executed once the email 
is sent. You will have to use the html command, <br>, to create a new line. Notice that 
whenever I switch to a new line inside python, I always leave a space at the end of the line 
so that the last word and the first word won't merge together.
<br><br>

You can also add a <a href="https://www.w3schools.com/html/html_links.asp">hyperlink</a> using 
html command. If you want any more customized text, search for the implementation in html!
<br><br>

Hope you enjoy!
<br><br>

Sissi Zhang
<br><br><br>
'''

recipients_file_path = r'C:\Users\...\recipients.txt'

recipients = []

with open(recipients_file_path, 'r') as recipients_file:
    recipient_data = recipients_file.readline()
    while recipient_data:
        if recipient_data.startswith('#'):
            recipient_data = recipients_file.readline()
            continue
        else:
            name, email = recipient_data.split(';')
            recipients.append({'name':name.strip(), 'email':email.strip()})
            recipient_data = recipients_file.readline()

# this is how this list will look like:
'''
recipients = [
    {'name': 'Recipient 1', 'email': 'example1@email.address'},
    {'name': 'Recipient 2', 'email': 'example2@email.address'},
    # Add more recipients as needed
]'''

# the name for the attachment here should match the actual file
attachment_file_path = r'C:\Users\...\picture template.png'


def main():

    for r in recipients:
        # personalizing the email body
        body_new = body.format(name=r['name']) 
        email_receiver = r['email']

        # creating the email
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body_new, 'html')

        # add an attachment
        with open(attachment_file_path, 'rb') as attachment_file:
            attachment_data = attachment_file.read()
            em.add_attachment(attachment_data, maintype='image', subtype='png', filename='Cat Image')
            # the name for the attachment here is the one that will appear on the recipient's email

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        # checking for one email is sent
        print(r['name'], 'done')


if __name__ == '__main__':
    main()
