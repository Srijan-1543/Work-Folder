import requests
from bs4 import BeautifulSoup

print("code working")
url = "https://www.imdb.com/list/ls058654847/"
req = requests.get(url)
content = req.content
soup=BeautifulSoup(content,"html.parser")
all_items = soup.find_all("div", {"class":"lister-item mode-detail"} )

print(soup.title.text)

for item in all_items:
    item_info = item.find("h3", {"class": "lister-item-header"})
    name = item_info.find("a").text
    no = item_info.find("span", {"class":"lister-item-index unbold text-primary"}).text
    print(no,name)
   

