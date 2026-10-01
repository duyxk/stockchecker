import requests 
from bs4 import BeautifulSoup
from time import *
from email.message import *
import smtplib

SMTP_SERVER = "smtp.gmail.com"        #gmail smtp server 
SMTP_PORT = 465 
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password" 
RECEIVER_EMAIL = "recipient@example.com"
msg = EmailMessage()

msg["Subject"] = "ITEM IN STOCK"
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL
msg.set_content("The item you are monitoring is now in stock!")

a = input("URL of the item you are checking for it's availabily:")
while True:
    r = requests.get(a)
    l = r.text
    soup = BeautifulSoup(l, 'html.parser')
    x = soup.find_all("script", type="application/ld+json")
    #x = print(soup.get_text())
    #x = soup.find_all('script')       
    #tag = soup.b
    #x = tag.script                         -- a set of failed tries(first tiem using bs4 // inexperienced with HTML)
    #print(x)
    def send_message(msg):
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)

    typeofx = type(x)
    #print (typeofx)
    x = str(x)
    typeofx = type(x)
    #print (typeofx)
    if "https://schema.org/InStock" in x:
            print("opla")
            send_message(msg)

    else:
        print("no")
    sleep(1)
