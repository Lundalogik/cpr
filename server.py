import bottle
from bottle import response
from bottle import redirect
from bottle import static_file

import os
import json

from articleHandler import ArticleLoader
from emailHandler import SendEmail


articles = ArticleLoader().load_articles_from_files("articles/")
SendEmail("filip.persson@.com", articles)


cpr = bottle.app()

@cpr.route('/')
def send_static():
    return static_file('/index.html', root='./')

@cpr.route('/articles')
def send_static():
    return articles 


cpr.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))