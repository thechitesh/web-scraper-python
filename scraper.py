import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.amazon.in/Nikon-AF-S-Nikkor-14-24mm-Camera/dp/B000VDCTCI/ref=sr_1_15?dchild=1&keywords=nikon+prime+lens+85mm&qid=1605346253&sr=8-15'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').getText()
    price = soup.find(id='priceblock_ourprice').getText()
    price = price.replace(',','')
    converted_price = float(price[2:10])
    
    print(title.strip())
    print(converted_price)

    if(converted_price < 150000):
        send_email()


def send_email():
    #tcktgsdmovqzssze
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('hi.alpha01@gmail.com', 'tcktgsdmovqzssze')
    # server.login('hi.alpha01@gmail.com', 'app_password')
    subject = "Price fell down for "
    body = 'Check the amazon link '+URL

    msg = f"Subject: {subject} \n\n {body}"
    server.sendmail(
        'hi.alpha01@gmail.com',  # from mail
        'thechitesh@gmail.com',  # to mail
        msg
    )
    print('Email has been sent')
    server.quit()

check_price()