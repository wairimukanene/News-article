from app import app
import urllib.request,json
from app.models import Source,Articles

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config['NEWS_SOURCES_BASE_URL']
articles_url = app.config['ARTICLES_BASE_URL']
