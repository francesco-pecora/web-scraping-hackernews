import requests                # allows us to gather html data
from bs4 import BeautifulSoup  # allows us to process html data
from flask import Flask, render_template
app = Flask(__name__)

res = requests.get('https://news.ycombinator.com')
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

top_news = create_custom_hackernews(links, subtexts)

def create_html_object(list):
    li = ''
    for item in list:
        # building the html object. Every iteration new <li> added
        li += "<li>" + "TITLE: " + item['title'] + "<br><a href=\"" + item['link'] + "\" target=\"_blank\">Link</a><br>Votes: " + str(item['votes']) + "<br><br></li>"
    return li

@app.route('/')
def home_route(html = None):
    return render_template('home.html', html = create_html_object(top_news))

if __name__ == '__main__':
    app.run(debug = True)

