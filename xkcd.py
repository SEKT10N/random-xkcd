from bs4 import BeautifulSoup
from random import randint
import requests
import webbrowser
import subprocess as sp
#import sys

sp.run('cls || clear', shell=True)

#connection_check = sp.getoutput("ping -n 1 goo.gl > %temp%/$null")

#if connection_check:
#    sys.exit("Please connect to the Internet and try again..")

termux = sp.getoutput('echo $PREFIX')

if termux:
   webbrowser.register("termux-open '%s'", None)
 
def get_xkcd():
    try:
        xkcd = randint(0,9999)
        URL = "https://xkcd.com/" + str(xkcd)
        #print(xkcd, URL)
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        title = soup.find(id="ctitle")
        img_url = soup.find(id="comic").find("img")
        img_url = "https:" + img_url['src']
   
        print(f"\n#{xkcd} {title.text.strip()}\n")       
        webbrowser.open(img_url)
    except:
        get_xkcd()

get_xkcd()