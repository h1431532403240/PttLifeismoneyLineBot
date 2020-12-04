import requests
from bs4 import BeautifulSoup

#將網頁資料GET下來
read = requests.get("https://www.ptt.cc/bbs/Lifeismoney/index.html").text
read = read[:read.find('<div class="r-list-sep"></div>')]

#將網頁資料以html.parser
soup = BeautifulSoup(read,"html.parser")

#取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
sel = soup.select("div.r-ent")

#取出超連結
for s in sel:
    #取得文章連結
    title = s.select("div.title a")
    href = title[0].get("href")
    print(href)
    #取得推文數
    push = s.select("div.nrec span")
    if push:
        nrec = push[0].text
    else:
        nrec = 0
    print(nrec)