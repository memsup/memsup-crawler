import requests
from bs4 import BeautifulSoup
import urllib3
import codecs
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

page = requests.get(
    f"https://tureng.com/en/turkish-english/{sys.argv[1]}",
    headers=headers,
    timeout=(20, 20),
    verify=False,
)

if page.status_code == 200:
    soup = BeautifulSoup(page.text, "html.parser")
    list = soup.find_all("div", class_="tureng-voice")
    if list:
        for i in list:
            for child in i.findChildren("audio", recursive=True):
                for subchild in child.findChildren("source", recursive=False):
                    print(subchild)
    else:
        print('404')
else:
    print('404')