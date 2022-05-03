from app import app
import urllib.request,json
from app.models import Source,Articles



#Getting api key
api_key = None

#Getting the source base url
base_url = None

#Getting the articles base url
articles_url = None


def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']

def get_sources(category):
  '''
  Function that gets the json response to our url request
  '''

