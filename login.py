# Jangan lupa instal dependencinya dulu
# instal requests -> pip install requests
# instal beautifoulsoup -> pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import userx # ambil username dan password dari file lain

url_login = ("https://my.smartfren.com/mysmartfren_login/login")
url_home = ("https://my.smartfren.com/mysmartfren_home")
# payload = {
#   "userid": "adi.trisoft@gmail.com",
#   "pass": "rahasia"
# }

#ambil dari file userx.py
payload = {
  "userid": userx.userid,
  "pass": userx.passx
}
#login dengan payload dan url di atas tanpa session
# r = requests.post(url_login,data=payload)
# print(r.text)

# login dengan session
with requests.session() as s:
    s.post(url_login,data=payload)
    # melaju ke halaman beranda
    r = s.get(url_home)
    # parser html
    soup = BeautifulSoup(r.content,'html.parser')

    #ambil data rincian paket
    datae = soup.find_all("tr") #tampilkan list table untuk menampilkan semua data dari tag htmlnya
   
    #buat looping untuk tampilkan dari td
    for d in datae:
        # print (d.find_all("td")[0].get_text()) #tampilkan teks aja tanpa tag html baris pertama
        # print (d.find_all("td")[2].get_text()) #tampilkan teks aja baris ke 3 
        print (d.find_all("td")[0].get_text()+" - "+d.find_all("td")[2].get_text()) #tampilkan teks aja baris ke 3 dengan di filter kata gb

