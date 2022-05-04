from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_article
from ..models import Source,Articles


# Views
@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''

  #Getting business related sources
  business_sources = get_sources()


  title = 'The Daily News'
  
  return render_template('index.html', title = title, business_sources = business_sources)

@main.route('/source/<id>')
def articles(id):

  '''
  View  articles function that returns a list of articles on the article

  '''
  articles = get_article(id)
  title = f'Headline {id}'

  print(articles)

  return render_template('article.html',title = title, articles = articles)

