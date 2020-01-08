from flask import render_template
from app import app
from .request import get_top_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    top_news = get_top_news()
    print(top_news)
    return render_template('index.html',top_news = top_news)