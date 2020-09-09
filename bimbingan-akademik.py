import requests
from bs4 import BeautifulSoup

username = 'isidenganusername'
password = 'isidenganpassword'
pesan_bimbingan = 'Tetap fokus dan siapkan yang terbaik. Bimbingan personal bisa melalui wa.me/628567074554'

s = requests.Session()
r = s.get("https://portal.pknstan.ac.id/")
if r.status_code==200:
    r = s.post('https://portal.pknstan.ac.id/auth/masuk', 
                           data={'identity': username, 'password': password, 'submit': 'Masuk'})
    if r.status_code==200:
        r = s.get("https://portal.pknstan.ac.id/lect/bimakad/dashboard")
        if r.status_code==200:
            # populate id_topik
            bsoup = BeautifulSoup(r.text, 'html.parser')
            #print(bsoup)
            id_topiks = bsoup.find_all("a", {"class": "reply-topik"})
            for id_topik in id_topiks:
                print(f"Reply to id topik: {id_topik}")
                r = s.post('https://portal.pknstan.ac.id/lect/bimakad/dashboard', 
                           data={'id_topik': id_topik['id'], 'topik': pesan_bimbingan, 'kirim': 'Balas Topik'})
