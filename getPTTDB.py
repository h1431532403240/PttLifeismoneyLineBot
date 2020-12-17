import requests
import urllib.parse
from requests_html import HTML
from bs4 import BeautifulSoup

def get_ptt_data():
    # 將網頁資料GET下來
    url = 'https://www.ptt.cc/bbs/Lifeismoney/index.html'
    read = HTML(html=requests.get(url).text)
    controls = read.find('.action-bar a.btn.wide')
    link = controls[1].attrs.get('href')
    page_url = urllib.parse.urljoin('https://www.ptt.cc/', link)
    get_main_data(url)
    get_main_data(page_url)

def get_main_data(url):
    # 將網頁資料GET下來
    read = requests.get(url).text
    read = read[:read.find('<div class="r-list-sep"></div>')]

    # 將網頁資料以html.parser
    soup = BeautifulSoup(read,'html.parser')

    # 取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
    sel = soup.select('div.r-ent')

    # 取出超連結
    for s in sel:
        # 取得文章連結
        title = s.select('div.title a')
        if title:
            href = title[0].get('href')
        else:
            continue
        print(href)
        # 取得推文數
        push = s.select('div.nrec span')
        if push:
            if push == '爆':
                nrec = 100
            elif push == 'X1':
                nrec = -10
            elif push == 'X2':
                nrec = -20
            elif push == 'X3':
                nrec = -30
            elif push == 'X4':
                nrec = -40
            elif push == 'X5':
                nrec = -50
            elif push == 'X6':
                nrec = -60
            elif push == 'X7':
                nrec = -70
            elif push == 'X8':
                nrec = -80
            elif push == 'X9':
                nrec = -90
            elif push == 'XX':
                nrec = -100
            else:
                nrec = push[0].text
        else:
            nrec = 0
        print(nrec)
        # 取得文章日期
        date = s.select('div.date')
        print(date[0].string)

get_ptt_data()