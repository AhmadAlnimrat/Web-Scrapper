#importing require libraries
from bs4 import BeautifulSoup
import requests


#Adding a username,password & the url
username, password = 'USERNAME', 'PASSWORD'
url  = "https://sandbox.oxylabs.io/products"
payload = {
    'source': 'universal_ecommerce',
    'render': 'html',
    'url': url,
}


#make a response by a request with a status code
response = requests.post(
    'https://realtime.oxylabs.io/v1/queries',
    auth=(username, password),
    json=payload,
)

#scrapping content and having output as html
content = response.json()["results"][0]["content"]
soup = BeautifulSoup(content, "html.parser")

#making a data list
data = []
for elem in soup.find_all("div", {"class": "product-card"}):
    title = elem.find('h4', {"class": "title"}).get_text(strip=True)
    price = elem.find('div', {"class": "price-wrapper"}).get_text(strip=True)


    #filling the data
    availability = elem.find('p', {"class": ["in-stock", "out-of-stock"]}).get_text(strip=True)
    data.append({
        "title": title,
        "price": price,
        "availability": availability,
    })
print(data)
