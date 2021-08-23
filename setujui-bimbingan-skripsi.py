import requests
from bs4 import BeautifulSoup
import datetime
import urllib3
import time 
import pytz

session = None
jakarta = pytz.timezone('Asia/Jakarta')

def set_global_session():
    global session
    if not session:
        session = requests.Session()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        session.verify = False
    return True

def login(username, password):
    with session.get('https://portal.pknstan.ac.id/') as response:
        if response.status_code == 200:
            with session.post('https://portal.pknstan.ac.id/auth/masuk', 
                              data={'identity': username, 'password': password, 'submit': 'Masuk'}) as response:
              print(response.text)
              if response.status_code==200 and len(response.text) != 0:
                  return True
              else:
                  return False
def logout():
    with session.get('https://portal.pknstan.ac.id/auth/logout') as response:
        #print(response.text)
        return True

def cek_id_bimbingan_skripsi():
    with session.get('https://portal.pknstan.ac.id/lect/lapbimbing') as response:
        #print(response.text)
        id_bimbingans = []
        for id_bimbingan in bsoup.find_all("button", string="setujui"):
            id_bimbingans.append(id_bimbingan['id']) 
        return id_bimbingans

def setuju_bimbingan_skripsi(ids):
    for id_bimbingan in ids:
      with session.post('https://portal.pknstan.ac.id/lect/lapbimbing/se7bimbing', data={'id': id_bimbingan}) as response:
          print("Setujui id bimbingan: " + id_bimbingan)
                     
if __name__ == "__main__":
    username = ''
    password = ''
    set_global_session()
    start_time = datetime.datetime.now()
    print("Start script in " + datetime.date.today().strftime("%-d-%m-%Y") + " at " + str(start_time))
    login(username, password)
    print("Ditemukan " + str(len(cek_id_bimbingan_skripsi())) + " bimbingan belum disetujui")
    setuju_bimbingan_skripsi(cek_id_bimbingan_skripsi())
    logout()   
    duration = datetime.datetime.now() - start_time
    print("Duration: " + str(duration))
