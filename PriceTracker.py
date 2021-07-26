import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/dp/B087JY84QQ/ref=s9_acss_bw_pg_test_2_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-5&pf_rd_r=6SCA01Y8WS8DACSA114A&pf_rd_t=101&pf_rd_p=7a1d8318-cf85-4bbe-a69b-0064cd342a79&pf_rd_i=22817284031'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def check_price():
        
    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title =  soup.find(id = 'productTitle').get_text()
    price = soup.find(id= "priceblock_ourprice").get_text()
    converted_price = float((price[1:7]).replace(',',''))
    if converted_price < 27000:
        send_mail()
        print(converted_price)
        print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('***@gmail.com','****')
    subject = 'Price fell down'
    body = 'Check the link https://www.amazon.in/dp/B087JY84QQ/ref=s9_acss_bw_pg_test_2_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-5&pf_rd_r=6SCA01Y8WS8DACSA114A&pf_rd_t=101&pf_rd_p=7a1d8318-cf85-4bbe-a69b-0064cd342a79&pf_rd_i=22817284031'

    msg =f"Subject:{subject}\n\n{body}"

    server.sendmail('****@gmail.com','****@gmail.com',msg)
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

while(True):
    check_price()
    time.sleep(60*60)
