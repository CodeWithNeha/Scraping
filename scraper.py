import requests
from bs4 import BeautifulSoup as bs
import csv

URL = 'https://www.youtube.com/'
req = requests.get(URL)
soup = bs(req.text, 'html.parser')
titles = soup.find_all('a')
titles_list = []

count = 1
for title in titles:
    d = {}
    d['Sr. Number'] = f'{count}'
    d['Anchor tag Name'] = title.text
    d['link'] = title.get('href')
    count += 1
    titles_list.append(d)

filename = 'titles.csv'
with open(filename, 'w', newline='') as f:
	w = csv.DictWriter(f,['Sr. Number','Anchor tag Name','link'])
	w.writeheader()
	
	w.writerows(titles_list)
