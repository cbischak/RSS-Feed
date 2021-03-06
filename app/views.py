from flask import render_template
from app import app
import feedparser
import datetime
import PyRSS2Gen
d = feedparser.parse('http://www.reddit.com/r/technology/.rss')
e = feedparser.parse('http://blogs.oracle.com/main/feed/entries/atom')
@app.route('/')
@app.route('/index')
def index():
    
    rss=[]
    for post in d.entries:
        rss.append(post.title+":"+post.link+"/n")
    
    atom=[]
    for post in e.entries:
        atom.append(post.title+":"+post.link+"/n")
    
    return render_template("index.html", title="Home", rss=rss, atom=atom)
@app.route('/feeder')
def feed(): 
    return render_template("feeder.html", title="feeder")
    

