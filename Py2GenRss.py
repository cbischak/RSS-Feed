import datetime
import PyRSS2Gen

rss = PyRSS2Gen.RSS2(
    title = "Center for Open Science RSS Feed",
    link = "http://centerforopenscience.org/press/",
    description = "The latest press about the Center for Open Science ",
                  

    lastBuildDate = datetime.datetime.now(),

    items = [
       PyRSS2Gen.RSSItem(
         title = "The Changing Face of Psychology",
         link = "http://www.theguardian.com/science/head-quarters/2014/jan/24/the-changing-face-of-psychology",
         description = "Psychology leading reforms, "
                       "that will benefit all of life sciences ",
         guid = PyRSS2Gen.Guid("http://www.theguardian.com/science/head-quarters/2014/jan/24/the-changing-face-of-psychology"),
         pubDate = datetime.datetime(2014, 1, 24, 14, 01)),
       PyRSS2Gen.RSSItem(
         title = "COS on NBC29",
         link = "http://www.nbc29.com/story/24468145/new-charlottesville-nonprofit-helps-scientists-collaborate-around-the-world"
                "archive/2003/09/06/RSS.html",
         description = "New Charlottesville Nonprofit "
                       "helps scientists collaborate ",
         
         guid = PyRSS2Gen.Guid("http://www.nbc29.com/story/"
         "24468145/new-charlottesville-nonprofit-helps-scientists-collaborate-around-the-world"),
         
         pubDate = datetime.datetime(2014, 1, 26, 06, 21)),
    ])

rss.write_xml(open("pyrss2genCOS.xml", "w"))