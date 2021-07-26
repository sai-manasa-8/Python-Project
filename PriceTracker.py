import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = input("Enter product URL to get price:\n")

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def check_price():
        
    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title =  soup.find(id = 'productTitle').get_text()
    price = soup.find(id= "priceblock_dealprice").get_text()
    converted_price = float((price[1:7]).replace(',',''))
    if converted_price < 27000:
        send_mail(converted_price)
        print(converted_price)
        print(title.strip())

def send_mail(converted_price):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('****@gmail.com','****')
    subject = 'Price fell down'
    body = 'Check the link'+URL
    new_price = converted_price
    msg =f"Subject:{subject}\n\n{body}\n\nPrice: Rs.{new_price}"

    server.sendmail('*****@gmail.com','*****@gmail.com',msg)
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

while(True):
    check_price()
    time.sleep(60*60)
    
