import os
from email.message import EmailMessage
import ssl
import smtplib

################################################# SENDER #################################################

email_sender = "example_email@gmail.com"
email_password = "the a 16-character password you set up"

################################################# CONTENT #################################################

subject = "Example Email Headline"
body = '''
<p style="font-size: 16px; font-family: Arial">
Dear {name}, <br>
<br>
{0} Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra 
maecenas accumsan lacus vel facilisis. <br>
<br>
{1} Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra 
maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices 
gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis. <br>
<br>
Sincerely, <br>
Your Name <br>
'''

################################################# ATTACHMENT #################################################

attachment_path = None
# the name for the attachment here should match the actual file
#attachment_path = r'C:\Users\...\picture template.png'
attachment_type = "image"
attachment_subtype = "png"
# the name for the attachment here is the one that will appear on the recipient's email
attachment_name = "Cat Image"

################################################# RECEIVERS #################################################

recipients_path = r'C:\Users\...\recipients.txt'

recipients = []

with open(recipients_path, 'r') as recipients_file:
    line = recipients_file.readline()
    while line:
        if line.startswith('#') or line == "\n":
            line = recipients_file.readline()
            continue
        else:
            temp_storage = line.split(';')
            name, email = temp_storage[0], temp_storage[1]
            messages = []
            if len(temp_storage > 2):
                for message in temp_storage[2:]:
                    messages.append(message)
            recipients.append({"name":name.strip(), "email":email.strip(), "message":messages})
            line = recipients_file.readline()

# this is how this list will look like:
'''
recipients = [
    {"name": 'Name 1', "email": 'name1@gmail.com', "message": [...]},
    {"name": 'Name 2', "email": 'name2@gmail.com', "message": [...]},
    # Add more recipients as needed
]'''

################################################# MAIN #################################################

def main():
    for person in recipients:
        # setting up the email
        body_formatted = body.format(name = person["name"]) 
        email_receiver = person["email"]

        if messages != []:
            for i in len(messages):
                body_formatted = body_formatted.format(i = messages[i])
                # "{0} {1}".format(10, 20) 

        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_receiver
        em["Subject"] = subject
        em.set_content(body_formatted, "html")
        
        if attachment_path != None: 
            with open(attachment_path, "rb") as attachment_file:
                attachment_data = attachment_file.read()
                em.add_attachment(attachment_data, maintype=attachment_type, \
                                  subtype=attachment_subtype, filename=attachment_name)

        context = ssl.create_default_context()

        #sending the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        print(person["name"], "done")

if __name__ == "__main__":
    main()
