import os
import yaml

class Article:
  def __init__(self):
    self.name = None
    self.html = None
    self.sections = []
    self.link = None


class ArticleLoader:
  def __init__(self):
    self.articles = []

  def load_articles_from_files(self, baseDir):
    for dirname, dirnames, filenames in os.walk(baseDir):
      # print path to all subdirectories first.
      for subdirname in dirnames:
        print(subdirname)
        for articledir, articledirnames, articlefilenames in os.walk(os.path.join(dirname, subdirname)):
          art = Article()
          if 'article.json' in articlefilenames:
            articleFileData = yaml.load(open(os.path.join(dirname, subdirname)  + '/article.yaml'))
            art.name = articleFileData['name']
            art.link = articleFileData['link']
            art.section = articleFileData['sections']
          self.articles.append(art)

    return self.articles
