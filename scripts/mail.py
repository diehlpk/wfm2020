# Script for sending the mails to
# the speakers
#
# Configuration
# - config.yaml.example for the smtp connection
# - text.dat.example for the e-mail's text
#   The tags inside < > are replaced with the values
#   of the corresponding attributes in the bibtex
#   file 
#
# @author patrickdiehl@lsu.edu
# @year 2019
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import yaml, codecs
import sys  

# Activate the utf8 encoding 
#reload(sys)  
#sys.setdefaultencoding('utf8')

# read the template text for the mail's content
file = open("text.dat",'r')
plainText = file.read()

# Setting for the smtp connection
username= ""
server= ""
password= ""
port = -1
address = ""
subject = ""

print("Starting e-mail sending script")

# Read the yaml file with the configuration
# for the connection to the smtp server
with open("config.yaml",'r') as f:
    doc = yaml.load(f,Loader=yaml.BaseLoader)
    username = doc["Mail"]["user"]
    server = doc["Mail"]["server"]
    password = doc["Mail"]["pw"]
    port = int(doc["Mail"]["port"])
    address = doc["Mail"]["address"]
    subject = doc["Mail"]["subject"]
    print("Loading config data for", username, server, port,subject)
    
# Connect to the mail server
server = smtplib.SMTP_SSL(server, port)
server.login(username, password)
        
# Read the e-mail addresses
file = open("mail.dat",'r')


for line in file:
    print(line)
    
    
    to = line
    cc = ""
    bcc = ""

    rcpt = cc.split(",") + bcc.split(",") + [to]
    msg = MIMEMultipart("alternative")
    msg['From'] = address
    msg['To'] = to
    msg['Subject'] = subject
    msg['Bcc'] = bcc
    
    msg.attach(MIMEText(plainText.encode("utf-8"), 'plain', "utf8"))

    text = msg.as_string()
    server.sendmail(address, rcpt, text)

# Close the connection
server.quit()
