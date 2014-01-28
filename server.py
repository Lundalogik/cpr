import bottle
from bottle import response, redirect, static_file, request

import os
import json

from articleHandler import ArticleLoader
from emailHandler import SendEmail


articles = {}
articles['articles'] = ArticleLoader().load_articles_from_files("articles/")
#SendEmail("smtp.mandrillapp.com",os.environ["SMTP_USER"], os.environ["SMTP_PASSWORD"],  "lars.andersson@lundalogik.se","filip.persson@lundalogik.se", articles)

cpr = bottle.app()

@cpr.route('/')
def send_static():
    return static_file('/index.html', root='./web')


@cpr.route('/web/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./web')

@cpr.route('/articles',method='GET')
def get_articles():
    return articles

@cpr.route('/send',method='POST')
def send_articles():
    email = request.forms.get('email')
    name = request.forms.get('name')
    articles = json.loads(request.forms.get('articles'))
    print(articles)
    SendEmail("smtp.mandrillapp.com",os.environ["SMTP_USER"], os.environ["SMTP_PASSWORD"],  email ,"info@lundalogik.se", articles)

    redirect("/")
    
cpr.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))