import requests                # allows us to gather html data
from bs4 import BeautifulSoup  # allows us to process html data

res = requests.get('https://news.ycombinator.com/news')

soup_object = BeautifulSoup(res.text, 'html.parser')

# selecting title and vote html objects
links = soup_object.select('.storylink')
votes = soup_object.select('.score')

print(links[0])
print(votes[0])