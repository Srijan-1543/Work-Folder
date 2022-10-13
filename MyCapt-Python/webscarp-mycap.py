import requests
from bs4 import BeautifulSoup

print("code working")
oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/"
req = requests.get(oyo_url)
content = req.content
print(content)
soup=BeautifulSoup(content,"html.parser")

all_hotels = soup.find_all("div", {"class": "hotelCardListing"} )
print(all_hotels)

for hotel in all_hotels:
    print("loop working")
    hotel_name=hotel.find("h3", {"class":"listingHotelDescription__hotelName"})
    print(hotel_name)
