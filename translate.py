import requests
from bs4 import BeautifulSoup
import urllib3
import codecs
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}


keywords = []
translate = open('translate.txt', 'w+', encoding='utf-8')

with open('words.txt', "r", encoding='utf-8') as f:
    keywords = f.read().split()

counter = 0
for keyword in keywords:
    page = requests.get(
        f"https://tureng.com/en/turkish-english/{keyword}",
        headers=headers,
        timeout=(20, 20),
        verify=False,
    )
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")
        list = soup.find_all("td", class_="tr ts")
        if list:
            count=0
            tr = "|"
            for i in list:
                if count != 3:
                    tr =  tr + str(i.find(text=True)) + "|"
                else:
                    break
                count += 1
            translated = '\n' + keyword + " " + tr
            translate.write(translated)
            counter += 1
            print('counter is ', counter)
