import requests
from bs4 import BeautifulSoup

for i in range(9):
    url = "https://www.oyorooms.com/oyos-in-chandigarh?page={}".format(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    hotel_name = []
    name = soup.find_all("span", {"class": "newHotelCard__hotelName"})
    print("total no of rooms:{}".format(len(name)))
    for info in name:
        print info.text
        hotel_names = info.text
        hotel_name.append(info.text)

    hotel_address = []
    address = soup.find_all("span", {"class": "newHotelCard__hotelAddress"})
    for addresses in address:
        print addresses.text
        hotel_address.append(addresses.text)

    hotel_prise = []
    prise = soup.find_all("div", {"class": "newHotelCard__pricing u-fw6"})
    for prises in prise:
        b = prises.contents[0]
        print b
        hotel_prise.append(b)

    hotel_revisedprise = []
    revisedprise = soup.find_all("span", {"class": "newHotelCard__revisedPricing"})
    for revisedprises in revisedprise:
        print revisedprises.text
        hotel_revisedprise.append(revisedprises.text)

    hotel_discount = []
    off = soup.find_all("div", {"class": "newHotelCard__discount"})
    for offs in off:
        c = offs.contents[0]
        print c
        hotel_discount.append(c)

    hotel_link = []
    link = soup.find_all("a", {"class": "newHotelCard__hotelMeta"})
    for links in link:
        url2 = "https://www.oyorooms.com"
        d = url2 + links["href"]
        print d
        hotel_link.append(d)
