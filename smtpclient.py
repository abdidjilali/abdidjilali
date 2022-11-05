import smtplib                          # importing the library for the smtp proccessing

from email import encoders
from email.mime.text import MIMEText                                      # proccessing email
from email.mime.base import MIMEBase                                     # proccessing attachements
from email.mime.multipart import MIMEMultipart

provider = input("Enter the smtp server address : ")
server = smptlib.SMPT(provider,24)

addr = input("Enter the email address : ")
passwd = input("Enter the path to the password file : ")
with open('passwd','r') as f:
	passwd = f.read()
server.login(addr,passwd)
# Specifying the header
		
From = input(" From : ")
To = input(" To : ")
Subject = input(" Subject :  ")

server.ehlo()                                                              # main function to proccess the interaction with the smtp server

messg["From"] = From
messg["To"] = To
messg["Subject"] = Subject
		
# specifying the content

messg_cont = input("Enter the path to your message : ")
messg_attach = input("Enter the path to your attachment : ")
		
# proccessing the content to the required format

with open(messg_cont , "r") as f :
		messg_cont = f.read()
messg.attach(MIMEText(messg_cont , "plain"))
messg_attach = open(messg_attach , "rb")

		# building the email 

emb = MIMEBase("application" , "octet-stream").set_payload(messg_attach.read())
encoders.encode_base64(emb)
emb.add_header("Content-Disposition" , f"messg_attach ; messg_attach={messg_attach}")
messg.attach(messg_attach)
content = messg.as_string()

		# sending the email

server.sendmail(addr,To,content)
