import requests 
from bs4 import BeautifulSoup
from time import *
from email.message import *
import smtplib
sleeptime=30        #in minutes

SMTP_SERVER = "smtp.gmail.com"        #gmail smtp server 
SMTP_PORT = 465 
SENDER_EMAIL = ""
SENDER_PASSWORD = "" 
RECEIVER_EMAIL = ""


TheSubject = "ITEM IN STOCK"
contentofmessage="The item you are monitoring is now in stock!"






msg = EmailMessage()
msg["Subject"] = TheSubject
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL
msg.set_content(contentofmessage)

a = input("URL of the item you are checking for it's availabily: ")
sleeptimeinminutes = sleeptime*60
while True:
    r = requests.get(a)
    l = r.text
    soup = BeautifulSoup(l, 'html.parser')
    x = soup.find_all("script", type="application/ld+json")
    #x = print(soup.get_text())
    #x = soup.find_all('script')       
    #tag = soup.b
    #x = tag.script                         -- a set of failed tries(first tiem using bs4 // consequences of inexperience with HTML)
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
            print("Item is in stock, email sent.")
            send_message(msg)
            break
    
    else:
        print("Not in stock.")
    time2 = sleeptimeinminutes
    while time2 != 0:
        print(f"\rTime remaining until next check: {time2} seconds", end="", flush=True)
        time2 = time2-1
        sleep(1)
