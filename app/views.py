from flask import render_template
from app import app
import feedparser
d = feedparser.parse('http://www.reddit.com/r/news/.rss')

@app.route('/')
@app.route('/index')
def index():
    d = feedparser.parse('http://www.reddit.com/r/news/.rss')
    rss=[]
    for post in d.entries:
        rss.append(post.title+":"+post.link+"/n")
    return render_template("index.html", title="Home", rss=rss)
