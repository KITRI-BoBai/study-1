from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://entertain.naver.com/home")
bsObject = BeautifulSoup(html, "html.parser")

result = str(bsObject.find('div', class_='rank_lst'))

print(result)
#result=re.sub('<.+?>', '', result, 0).strip()
#print(result)