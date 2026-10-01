import requests 
from bs4 import BeautifulSoup
from time import *

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
    print(x)


    typeofx = type(x)
    print (typeofx)
    x = str(x)
    typeofx = type(x)
    print (typeofx)
    if "https://schema.org/InStock" in x:
            print("opla")
    else:
        print("no")
    sleep(30*60)
