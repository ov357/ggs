# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 07:58:45 2017
@author: milal
"""

from flask import Flask
from flask import render_template
from flask import request
#import redis
import feedparser
import random

app = Flask(__name__)

RSS_FEEDS = {'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn':'http://rss.cnn.com/rss/edition.rss',
             'fox':'http://feeds.foxnews.com/foxnews/latest',
             'iol':'http://iol.co.za/cmlink/1.640'}


def storedb():
    # store somethin into redis DB and persist the data
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set('foo', 'bar')


@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    feed=feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return """<html>
        <body>
            <h1>Headlines</h1>
            <b>{0}</b> </br>
            <i>{1}</i> </br>
            <p>{2}</p> </br>
        </body>
    </html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))

DEFAULTS = {'publication' : 'bbc',
            'city' : 'LONDON,UK'
    }

@app.route("/m4", methods = ['GET', 'POST'])
def m4(c=[0,1,2,3,4,5,6,7,8,9]):
    query = request.args.get("lt")
    if query:
        c = query.split(',')
        c = [0]+c
    c = [int(x) for x in c]
    #print('c=',type(c))
    # multis en 4 favos - c contient la liste type
    cbs = [
    		[1, 4, 2, 5],
    		[1, 4, 2, 9],
    		[1, 8, 2, 5],
    		[1, 8, 2, 9],
    		[1, 4, 2, 6],
    		[1, 4, 2, 7],
    		[1, 8, 2, 6],
    		[1, 8, 2, 7],
    		[2, 5, 3, 6],
    		[2, 5, 3, 7],
    		[2, 9, 3, 6],
    		[2, 9, 3, 7],
    		[2, 5, 3, 4],
    		[2, 5, 3, 8],
    		[2, 9, 3, 4],
    		[2, 9, 3, 8],
    		[3, 6, 1, 4],
    		[3, 6, 1, 8],
    		[3, 7, 1, 4],
    		[3, 7, 1, 8],
    		[3, 6, 1, 5],
    		[3, 6, 1, 9],
    		[3, 7, 1, 5],
    		[3, 7, 1, 9],
    	]
    l = [0,1,2]
    #print(r[:],c)
    combs = []
    for e1,i in enumerate(cbs):
        p = random.sample(l[:3],2)
        if (2 in p):
            c1 = []
            for j in i:
                #print(c[j], end='-')
                c1.append(c[j])
            #print()
            combs.append(c1)
    #print(combs)
    return render_template("m4.html", combs = combs)


@app.route("/m4", methods = ['GET', 'POST'])
def m4(c=[0,1,2,3,4,5,6,7,8,9]):
    query = request.args.get("lt")
    #print(type(c))
    if query:
        c = query.split(',')
        c = [0]+c
        c = [int(x) for x in c]
        #print(type(c))
    #print('c=',type(c))
    # multis en 4 favos - c contient la liste type
    cbs = [
    		[1, 4, 2, 5],
    		[1, 4, 2, 9],
    		[1, 8, 2, 5],
    		[1, 8, 2, 9],
    		[1, 4, 2, 6],
    		[1, 4, 2, 7],
    		[1, 8, 2, 6],
    		[1, 8, 2, 7],
    		[2, 5, 3, 6],
    		[2, 5, 3, 7],
    		[2, 9, 3, 6],
    		[2, 9, 3, 7],
    		[2, 5, 3, 4],
    		[2, 5, 3, 8],
    		[2, 9, 3, 4],
    		[2, 9, 3, 8],
    		[3, 6, 1, 4],
    		[3, 6, 1, 8],
    		[3, 7, 1, 4],
    		[3, 7, 1, 8],
    		[3, 6, 1, 5],
    		[3, 6, 1, 9],
    		[3, 7, 1, 5],
    		[3, 7, 1, 9],
    	]
    l = [0,1,2]
    #print(r[:],c)
    combs = []
    for e1,i in enumerate(cbs):
        p = random.sample(l[:3],2)
        if (2 in p):
            c1 = []
            for j in i:
                #print(c[j], end='-')
                c1.append(c[j])
            #print()
            combs.append(c1)
    print(combs)
    return render_template("m4.html", combs = combs)


def index():
    # storedb()
    return "Hello World!"


if __name__ == '__main__':
    app.run(port=8000, debug=True)
