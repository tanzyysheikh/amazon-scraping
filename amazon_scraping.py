import requests
from bs4 import BeautifulSoup
import smtplib
import re

url = 'https://www.amazon.in/Apple-iPhone-Pro-Max-64GB/dp/B07XVLMZHH/ref=sr_1_3?crid=20RW3AUCZEX5E&dchild=1&keywords=iphone+11+pro+max+512gb&qid=1597060577&s=electronics&sprefix=iphone%2Celectronics%2C517&sr=1-3'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}

#Checks if the price of product has dropped
def track_price():
    page = requests.get(url, headers = headers)

    soup = BeautifulSoup(page.content, "html.parser")


    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text().replace(',', '')

    print(price)
    converted_price = float(price[2:])

    if(converted_price < 11500):
        send_mail()
    else:
        print("Sorry the price is too high! ")
#Sends an email when price drops
def send_mail():
    email = input("Enter your email address:\n")
    password = input("Enter 2-step verification password:\n")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(email, password)

    sub = "Price fell down!"

    body = "Quick link to purchase: "+url

    msg = f"Subject: {sub}\n\n{body}"

    server.sendmail(email, email, msg)

    print("Hey email has been sent!")

    server.quit()

track_price()