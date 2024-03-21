import email, smtplib, ssl
from providers import PROVIDERS
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.message import EmailMessage

from email import encoders

from os.path import basename

import json
# before use must ensure gmail has enabled third party addons
# to do this go to https://myaccount.google.com/ -> security -> enable two step verifcation
# once you are done click on two step verification again -> app passwords ->name it anythign (name doesnt matter)
# it will give you a temporary password like irpx bpmu ozne fybr which you put into passwords

# For phones you text to email using https://www.digitaltrends.com/mobile/how-to-send-a-text-from-your-email-account/
# note you will need to know the carieer. Note better to use other python code to do this. This mainly for
# sending emails


def send_email(
        receiver_email:str, 
        subject: str,
        message: str,
        sender_credentials_: tuple,
        smtp_server: str = "smtp.gmail.com",
        smpt_port: int = 465):
    sender_email, email_password = sender_credentials_
    email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"
    with smtplib.SMTP_SSL(smtp_server, smpt_port, context=ssl.create_default_context()) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_credentials_, receiver_email, email_message)

def send_email_attachments(
        receiver_email:str, 
        subject: str,
        message: str,
        files:list[str],
        sender_credentials_: tuple,
        smtp_server: str = "smtp.gmail.com",
        smpt_port: int = 465):
    sender_email, email_password = sender_credentials_
    email_message = EmailMessage()
    email_message["Subject"]=subject
    email_message["To"]=receiver_email
    email_message["From"]=sender_email
    email_message.attach(MIMEText(message, "plain"))
    for filename in files:
        filetype=filename.split('.')
        filetype=filename[1]
        if filetype=="JPG" or filetype=="jpg" or filetype=="png" or filetype=="PNG":
            import imghdr
            with open(filename,'rb') as f:
                file_data= f.read()
                image_type=imghdr.what(filename)
            email_message.add_attachment(file_data,maintype='image',subtype=image_type,filename=f.name)
        else:
            with open(filename,'rb') as f:
                file_data= f.read()
            email_message.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=f.name)
    with smtplib.SMTP_SSL(smtp_server, smpt_port,context=ssl.create_default_context()) as email:
        email.login(sender_email,email_password)
        email.send_message(email_message)

#used for testing code 
def main():
    #number you are sending to and message along with provider of the pearson you send message to 
    email= "david123hao@gmail.com"
    message="hellow world"
    subject="test"
    #gmail and temporary password (look above for information)
    sender_credentials = ("nyupideltapsi@gmail.com", "irpx bpmu ozne fybr")
    
    # uncoment below for sms
    #send_mms_via_email(number, message, provider, sender_credentials)

    #these are needed for mms 
    files=["Garfeef.png","instructions.txt"]
    send_email_attachments(email,subject,message,files, sender_credentials)

if __name__=="__main__":
    main()