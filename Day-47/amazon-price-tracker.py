from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
RECIPIENT_EMAIL = "rbrs1116@yahoo.com.ph"

header_params = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding":"gzip, deflate, br, zstd",
    "priority":"u=0, i",
    "sec-fetch-dest":"document",
    "sec-fetch-mode":"navigate",
    "sec-fetch-site":"cross-site",
    "sec-fetch-user":"?1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9",
    "upgrade-insecure-requests":"1"
}

response = requests.get(url=URL, headers=header_params)
sp = BeautifulSoup(response.text, "html.parser")
price_symbol = sp.find("span", class_="a-price-symbol").getText()
price_whole_num = sp.find("span", class_="a-price-whole").getText().split(".")[0]
price_frac_num = sp.find("span", class_="a-price-fraction").getText()
price = float(price_whole_num + "." + price_frac_num)
prod_name = " ".join(sp.find("span", id="productTitle").getText().split())
print(price)
print(prod_name)

if price <= 100:
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as smtp:
        smtp.starttls()
        smtp.login(user=os.environ["EMAIL_ADDRESS"], password=os.environ["EMAIL_PASSWORD"])
        smtp.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=RECIPIENT_EMAIL,
            msg=f"Subject:AMAZON PRICE ALERT!!!\n\n{prod_name} is now priced at {price_symbol}{price}\n{URL}!".encode("utf-8")
        )
