import os
import yaml

class ArticleLoader:
  def __init__(self):
    self.articles = []

  def load_articles_from_files(self, baseDir):
    for dirname, dirnames, filenames in os.walk(baseDir):
      # print path to all subdirectories first.
      for subdirname in dirnames:
        print(subdirname)
        for articledir, articledirnames, articlefilenames in os.walk(os.path.join(dirname, subdirname)):
          
          if 'article.yaml' in articlefilenames:
            articleFileData = yaml.load(open(os.path.join(dirname, subdirname)  + '/article.yaml'))
            self.articles.append(articleFileData)

    return self.articles
