import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders
import datetime
from typing import List
import os


def send_email(sender_email: str, sender_password: str, to_email: List[str], smtp_server: str = None, smtp_port: str = None, file_loc: str = None, mail_body: str = 'this is message generated from send_alert module', mail_subject: str = f"{datetime.datetime.now()} alert sent by send_alert module") -> bool:
    """
    sender_email : email you will use to send the alert\n
    sender_password : password for the email you will use to send the alert\n
    to_email : list of emails that will get the alert\n
    ex) ['test1@gmail.com','test2@gmail.com']\n
    smtp_server : smtp server for your sender email. If we have the smtp server of your email provider in our db, you might not need to input it  
    ex) gmail.com -> smtp.gmail.com
    smtp_port : smtp server for your sender email. If we have the smtp port of your email provider in our db, you might not need to input it 
    ex) gmail.com -> 587 
    file_loc : full directory of the attachement file (default : None)\n
    mail_body : the content of the mail\n
    mail_subject : the subject of the mail \n
    """

    # list of email providers
    email_provider_dict = {
        "gmail": {
            "smtp_server": "smtp.gmail.com",
            "smtp_port": 587
        },
        "yahoo": {
            "smtp_server": "smtp.mail.yahoo.com",
            "smtp_port": 465
        },
        "outlook": {
            "smtp_server": "smtp.office365.com",
            "smtp_port": 587
        },
        "aol": {
            "smtp_server": "smtp.aol.com",
            "smtp_port": 587
        },
        "protonmail": {
            "smtp_server": "smtp.protonmail.com",
            "smtp_port": 587
        },
        "naver": {
            "smtp_server": "smtp.naver.com",
            "smtp_port": 587
        },
        "zoho": {
            "smtp_server": "smtp.zoho.com",
            "port": 587
        }
    }
    # Email credentials
    sender_email = sender_email
    # If smtp_server or smtp_port is not provided
    if smtp_server is None or smtp_port is None:
        email_provider = sender_email.split('@')[1].split('.')[0].lower()
        try:
            smtp_server = email_provider_dict[email_provider]["smtp_server"]
            smtp_port = email_provider_dict[email_provider]["smtp_port"]
        except Exception as e:
            print("smtp_server and smtp_port was not found in our database. Please provide the server (eg. smtp.gmail.com) and the port (eg. 465)")
            print(e)
    sender_password = sender_password
    

    # Recipient email
    to = to_email

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = COMMASPACE.join([to])
    print(msg['To'])
    msg['Subject'] = mail_subject

    # Add message body
    body = mail_body
    msg.attach(MIMEText(body))

    if file_loc:
        # Add attachment
        filename = file_loc
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        "attachment; filename= %s" % filename)
        msg.attach(part)

    # Send the email
    try:
        smtpObj = smtplib.SMTP(smtp_server, smtp_port)
        smtpObj.starttls()
        smtpObj.login(sender_email, sender_password)
        smtpObj.sendmail(sender_email, to, msg.as_string())
        smtpObj.quit()
        print(f"Email to {to} sent successfully")
        return True
    except Exception as e:
        print("Error: unable to send email", e)
        return False



