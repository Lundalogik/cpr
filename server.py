import bottle
from bottle import response
from bottle import redirect
from bottle import static_file
import os
from articleHandler import ArticleLoader
from articleHandler import Article

articles = ArticleLoader().load_articles_from_files("articles/")
print(articles[0].name)

cpr = bottle.app()

@cpr.route('/')
def send_static():
    return static_file('/index.html', root='./')


cpr.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))