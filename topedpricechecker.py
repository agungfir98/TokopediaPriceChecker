import requests                             # melakukan request
from bs4 import BeautifulSoup               # library untuk parsing Html
import smtplib                              # untuk mengirim mail
import time                                 # waktu

URL = 'https://www.tokopedia.com/techstudioid/macbook-pro-2020-13-touch-bar-mwp42-mwp72-2-0ghz-4c-i5-16gb-512gb-space-grey'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}


def cekharga():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())                                # melihat isi html site

    judul = soup.find(attrs={"css-x7lc0h"}).get_text()
    harga = soup.find(attrs={"css-c820vl"}).get_text()
    konversi_harga = float(harga[2:].replace('.',''))       # Mneghilangkan titik "." pada harga dan Merubah harga(str) ke float


    print(judul)
    print(konversi_harga)

    harga_diharapkan = 32000000                             # Harga yang diharapkan.

    if (konversi_harga < harga_diharapkan):
        sendmail()
    else:
        print("gagal kirim mail")

# setup smtp
def sendmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('<EMAIL-PENGIRIM>', '<PASWORD>') # Login Mail pengirim

    # DRAFT Mail yang akan dikirim
    subject = "harga turun Bor!!!!"
    body = "Cek lay sokin.\n Link: https://www.tokopedia.com/techstudioid/macbook-pro-2020-13-touch-bar-mwp42-mwp72-2-0ghz-4c-i5-16gb-512gb-space-grey"

    message = f"Subject: {subject}\n\n {body}"
    
    server.sendmail(
        "EMAIL_PENGIRIM",
        "EMAIL_PENERIMA",
        message
    )
    print("Mail Terkirim!")

    server.quit()

# Looping untuk mengecek harga item yang diinginkan.
while True:
    cekharga()
    time.sleep(60*60)