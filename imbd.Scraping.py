
import requests
from bs4 import BeautifulSoup
import pandas as pd
data = []
url = "https://www.imdb.com/chart/toptv"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)


soup = BeautifulSoup(response.content, 'html.parser')
movies = soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 iyTDQy compact-list-view ipc-metadata-list--base").find_all('li')
    
for movie in movies:
       
        item = {}
        item['Serie'] = movie.find('div', class_="ipc-metadata-list-summary-item__c").a.text
        item['Tiempo en Aire'] = movie.find ('div', class_="sc-6ade9358-6 cBtpuV cli-title-metadata").span.text
        item['clasificacion'] = movie.find ('div', class_="sc-6ade9358-6 cBtpuV cli-title-metadata").get_text(strip=True).split(' ')[1]
        item['calificacion'] = movie.find ('div', class_="sc-e2dbc1a3-0 jeHPdh sc-6ade9358-3 byWcx cli-ratings-container").span.text
        
        data.append(item)
    
df = pd.DataFrame(data)
df.to_csv("top 25 de imdb.csv", index=False)
