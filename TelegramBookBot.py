import requests
from bs4 import BeautifulSoup
import re
import random
from time import sleep
import time
import traceback
import telebot
bot = telebot.TeleBot("1821217113:AAFdTsrfDnHbQCHMJ0RSS9NQTOGlrPWqeyQc")
channel_id = -1001570199213
@bot.message_handler(commands=['start'])
def welcome_help(message):
  while True:
    listNum = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
               '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36',
               '37',
               '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50','84','82']
    numberD = random.choice(listNum)
    url = f"https://www.kutub.info/library/category/{numberD}"
    payload = {}
    headers = {
      'Connection': 'keep-alive',
      'Cache-Control': 'max-age=0',
      'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
      'sec-ch-ua-mobile': '?0',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'Sec-Fetch-Site': 'none',
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-User': '?1',
      'Sec-Fetch-Dest': 'document',
      'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
      'Cookie': '_ga=GA1.2.1081912384.1628779964; _gid=GA1.2.456085246.1628779964; __gads=ID=daa59bef9e04fd22-220e875a9cc8004c:T=1628758392:RT=1628758392:S=ALNI_MZZThX0Vwdsr66i3Kv0fWbTlY1BwQ; _gat_gtag_UA_15777643_2=1; XSRF-TOKEN=eyJpdiI6IlBCbFpmVXhwbTF2ckxjWmpSSzVaNHc9PSIsInZhbHVlIjoiOTg3OFBkaHZZV2cxRFFaUTVyb0hsOHFFWllTRzdjUUpucHB0aEJVSElaM0xMRHVSM09VLzlkZnpUSzEvS3JtRDhuemxTV1V6bHR0R3JhRGtrL0pEY1pDWUR4TUlCY1l0eUFpUkxqQkVnSHNDa1ZPTG10eXlTcjdoZ2hwdk5VTk4iLCJtYWMiOiI4NjBhYjk2YjM4ZjM3OGMwYWE4ZTIyNjdhNGExZmQ3MzQ1OTgxOTI0N2VjNzQzM2NjYTA1YmE1MWJjYzc2NzE0In0%3D; kutub_session=eyJpdiI6Ik1SaUdKejRCSUZRejhXYWQwazBZWXc9PSIsInZhbHVlIjoiN0ZjQkpMS0dBRmNGMWo4MEFjbzlMUXZGd3FEQlRzdU9QcHNwc3dUbGRJTDFCWDAvYWxxUmVDVDRtZUY0RWhETXdlNTQ4VGJjRmxTNUgvaUllZXhBaHRLclB4UFlrVTIyNU8wZjNmY2R6S0FxR2FQVDI0YjBhaUpjN3JYdGo3NUQiLCJtYWMiOiIzZWI2MzY2OTJiYmIxNjMxYzliY2I5MmMwYzcxNzA4OGU3Njc1MDhkMDEyODFmYTU1MDdiYTQ1ZGJkODgyMWUyIn0%3D'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    s = BeautifulSoup(response.text, "html.parser")
    extractUrl = re.findall(r'(https?://www.kutub.info/library/book/\d+)', str(s))
    if extractUrl==None:
      pass
    else:
      do = random.choice(extractUrl)
      url1 = do
      payload1 = {}
      headers1 = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://www.kutub.info/library/category/7',
        'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
        'Cookie': '_ga=GA1.2.1081912384.1628779964; _gid=GA1.2.456085246.1628779964; __gads=ID=daa59bef9e04fd22-220e875a9cc8004c:T=1628758392:RT=1628758392:S=ALNI_MZZThX0Vwdsr66i3Kv0fWbTlY1BwQ; XSRF-TOKEN=eyJpdiI6Im5YY0Nya2FSUGFqNEc1WENHZENsM3c9PSIsInZhbHVlIjoidTN5OUUrM0NoeTVqT3pYeFQvcWhRMFV6aEJidDIzaVpWbUpMVzJ5NXByTlVjeWsyWGwyRzhpTVd4TDRGMEFWQVFVMHc5Tjc3Y0U5a1M2NWVhdmNneHNaTzFZNCtOUE92SDFULzEwWmY3YmQrSlNlZUNkaTZzQ0s0c0RvTE5pVnoiLCJtYWMiOiIyNTNlMzQyMjRiZTc5MTU1ZDQwODhmMmQ1MzA4NGM3YjM5ZDE4NGY2MWQ0MzhmNmFmYTRjZDgwYjBjMTdmODdjIn0%3D; kutub_session=eyJpdiI6IlY0N01pZlR4c2pHMmlQNVNLS2hYRVE9PSIsInZhbHVlIjoiaDZadHlMb2xDdUxFZllQWHpTc2MwV3ZoR1Fkb3JEbExKYk5RVVNhSFpkb3dkVE5JMGJSS1NDNVFuT0FUbXlyU2NOWlA4Njh3M1dPNitRYm8xSk1UQm91cmQ1UkhWVXJyRVRyZi9KcXF0ZzlVY0xxSGFHZXBLaUo0MEhXZlMrWTgiLCJtYWMiOiJkNmQyMmIyOWM1YTZkOGRmNTg3ZjM3ZTFjOWJmYmM0YWY5MmQ4YjgwODU5YTg3ZGEwMmRlMTZlN2Y2MmI0MDI0In0%3D; _gat_gtag_UA_15777643_2=1'
      }

      response1 = requests.request("GET", url1, headers=headers1, data=payload1)
      s1 = BeautifulSoup(response1.text, "html.parser")
      nameBook = s1.findAll('li', attrs={'class': 'breadcrumb-item active'})[0].text
      department = s1.findAll('div', class_='col-xs-12 col-md-9')[0].findAll('p')[2].contents[0]
      info = s1.findAll('div', class_='col-xs-12 col-md-9')[0].findAll('p')[4].contents[0]
      type = s1.findAll('div', class_='col-xs-12 col-md-9')[0].findAll('p')[16].contents[0]
      print(type)
      downloadFileSett = s1.find('div', attrs={'class': 'download'})
      for a in downloadFileSett.find_all('a', href=True):
        downloadFileGo = a['href']
        if ('zip') in str(type):
          print("zip")
          urldownload = downloadFileGo
          rD = requests.get(urldownload, stream=True, timeout=1000000)
          with open('book.zip', 'wb') as fd:
            for chunk in rD.iter_content(chunk_size=1024):
              fd.write(chunk)
          i = open('./book.zip', 'rb')
          bot.send_document(channel_id, i,
                            caption=f"*Name* 🗃 : {nameBook}\n------------\n*Department* 📂 : {department}\n------------\n*Info* 🧾 : {info}\n------------\n*Copyright* - t.me/bookinfoplus",
                            parse_mode='Markdown', timeout=1000000)
        elif ('pdf') or ('PDF') in str(type):
          print("pdf")
          urldownload = downloadFileGo
          rD = requests.get(urldownload, stream=True, timeout=1000000)
          with open('book.pdf', 'wb') as fd:
            for chunk in rD.iter_content(chunk_size=1024):
              fd.write(chunk)
          i = open('./book.pdf', 'rb')
          bot.send_document(channel_id, i,
                            caption=f"*Name* 🗃 : {nameBook}\n------------\n*Department* 📂 : {department}\n------------\n*Info* 🧾 : {info}\n------------\n*Copyright* - t.me/bookinfoplus",
                            parse_mode='Markdown', timeout=1000000)
        elif ('doc') in str(type):
          print("doc")
          urldownload = downloadFileGo
          rD = requests.get(urldownload, stream=True, timeout=1000000)
          with open('book.doc', 'wb') as fd:
            for chunk in rD.iter_content(chunk_size=1024):
              fd.write(chunk)
          i = open('./book.doc', 'rb')
          bot.send_document(channel_id, i,
                            caption=f"*Name* 🗃 : {nameBook}\n------------\n*Department* 📂 : {department}\n------------\n*Info* 🧾 : {info}\n------------\n*Copyright* - t.me/bookinfoplus",
                            parse_mode='Markdown', timeout=1000000)
        elif ('rar') in str(type):
          print("rar")
          urldownload = downloadFileGo
          rD = requests.get(urldownload, stream=True, timeout=1000000)
          with open('book.rar', 'wb') as fd:
            for chunk in rD.iter_content(chunk_size=1024):
              fd.write(chunk)
          i = open('./book.rar', 'rb')
          bot.send_document(channel_id, i,
                            caption=f"*Name* 🗃 : {nameBook}\n------------\n*Department* 📂 : {department}\n------------\n*Info* 🧾 : {info}\n------------\n*Copyright* - t.me/bookinfoplus",
                            parse_mode='Markdown', timeout=1000000)
        sleep(300)



bot.polling(none_stop=True)



