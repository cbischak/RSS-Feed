from flask import render_template
from app import app
import feedparser
d = feedparser.parse('http://www.reddit.com/r/news/.rss')
e = feedparser.parse('http://bblfish.net/blog/blog.atom')
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
