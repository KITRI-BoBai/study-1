import requests
from bs4 import BeautifulSoup as bs

url="https://entertain.naver.com/home"
response= requests.get(url)
text=response.text
soup=bs(text,'html.parser')
newslists=soup.select('.rank_lst')
for i in newslists:
    newslist=i.get_text()
    print(newslist)
