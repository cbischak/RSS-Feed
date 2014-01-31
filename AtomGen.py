from pyatom import AtomFeed
import datetime

feed = AtomFeed(title="Center for Open Science",
                subtitle="Example for a feed test.",
                feed_url="http://centerforopenscience.org/press/",
                url="http://centerforopenscience.org/",
                author="George Washington")

# Do this for each feed entry
feed.add(title="The Changing Face of Psychology",
         content="After 50 years of stagnation in research practices" 
         "psychology is leading reforms that will benefit all life sciences",
         content_type="html",
         author="George Washington",
         url="http://www.theguardian.com/science/head-quarters/2014/jan/24/the-changing-face-of-psychology",
         updated=datetime.datetime.utcnow())

x = feed.to_string()
output = (open("AtomGen.xml", "w"))
output.write(x)
 
