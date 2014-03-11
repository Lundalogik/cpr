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

@cpr.route('/test')
def send_static():
    return static_file('/test.html', root='./web')


@cpr.route('/web/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./web')

@cpr.route('/articles',method='GET')
def get_articles():
    return articles

@cpr.route('/send',method='POST')
def send_articles():
    email = {}
    email['from_address'] = "info@lundalogik.se"
    email['to_address'] = request.forms.get('email')
    email['server'] = "smtp.mandrillapp.com"
    email['user'] = os.environ["SMTP_USER"]
    email['password'] = os.environ["SMTP_PASSWORD"]
    print(os.environ["SMTP_PASSWORD"])
    print(email)
    selected_articles = json.loads(request.forms.get('articles'))

    name = request.forms.get('name')

    SendEmail(email,selected_articles)
    
    redirect("/")
    
cpr.run(host="0.0.0.0", server="gunicorn", port=int(os.environ.get("PORT", 5000)))