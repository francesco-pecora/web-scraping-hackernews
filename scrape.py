import requests                # allows us to gather html data
from bs4 import BeautifulSoup  # allows us to process html data
import pprint                  # nice output

res = requests.get('https://news.ycombinator.com/news')

soup_object = BeautifulSoup(res.text, 'html.parser')

# selecting title and vote html objects
links = soup_object.select('.storylink')
subtext = soup_object.select('.subtext')

def create_custom_hackernews(links, subtext):
    new_list = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None) # default value of None if no href
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', '')) # parsing to only get the numbers
            if points > 99:
                new_list.append({'title': title, 'link': href, 'votes': points})
    
    return new_list

#print(create_custom_hackernews(links, votes)[0])
pprint.pprint(create_custom_hackernews(links, subtext))