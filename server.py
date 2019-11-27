import scrape
from flask import Flask, render_template
app = Flask(__name__)

top_news = scrape.create_custom_hackernews(scrape.links, scrape.subtexts)

def create_html_object(list):
    li = ''
    for item in list:
        # building the html object. Every iteration new <li> added
        li += "<li>" + "TITLE: " + item['title'] + "<br><a href=\"" + item['link'] + "\" target=\"_blank\">Link</a><br>Votes: " + str(item['votes']) + "<br><br></li>"
    return li

@app.route('/')
def home_route(html = None):
    return render_template('home.html', html = create_html_object(top_news))

# running the application
if __name__ == '__main__':
    app.run(debug=True)
