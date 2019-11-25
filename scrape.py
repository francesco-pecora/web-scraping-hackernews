import requests                # allows us to gather html data
from bs4 import BeautifulSoup  # allows us to process html data
import pprint                  # nice output

res = requests.get('https://news.ycombinator.com/news')

soup_object = BeautifulSoup(res.text, 'html.parser')

# selecting title and vote html objects
links = soup_object.select('.storylink')
subtexts = soup_object.select('.subtext')

def sort_by_votes(list):
    # sorting by votes in ascending order
    return sorted(list, key = lambda k: k['votes'], reverse = True)

def create_custom_hackernews(links, subtexts):
    new_list = []
    for idx, item in enumerate(links):

        title = item.getText()
        href = item.get('href', None) # default value of None if no href
        vote = subtexts[idx].select('.score')

        # avoiding cases in which there are no votes
        if len(vote):
            points = int(vote[0].getText().replace(' points', '')) # parsing to only get the numbers
            
            # only appending titles with score of 100+
            if points > 99:
                new_list.append({'title': title, 'link': href, 'votes': points})
    
    return sort_by_votes(new_list)

#print(create_custom_hackernews(links, votes)[0])
pprint.pprint(create_custom_hackernews(links, subtexts))