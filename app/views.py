from flask import render_template
from app import app
from .request import get_sources,get_article

# Views
@app.route('/')
def index():
  
  '''
  View root page function that returns the index page and its data
  '''

  #Getting business related sources
business_sources = get_sources('business')

#Getting technology related sources
tech_sources = get_sources('technology')

#Getting sports related sources
sports_sources = get_sources('sports')


print(tech_sources)
title = 'The Daily News'



@app.route('/source/<id>')
def articles(id):

  '''
  View  articles function that returns a list of articles on the article

  '''
  articles = get_article(id)
  title = f'Headline {id}'

  return render_template('index.html', title=title, business = business_sources,technology=tech_sources,sports=sports_sources)



  


  
