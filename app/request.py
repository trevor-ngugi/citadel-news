from app import app
import urlib.request,json
from .models import article,source

Article=article.Article
Source=source.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

#getting the news base url
top_news_base_url=app.config['TOP_NEW_URL']
news_sources_base_url=app.config['NEWS_SOURCES_URL']

def get_top_news():
    '''
    Function that gets the json response to our url request
    '''
    get_top_news_url=top_news_base_url.format(api_key)

    with urlib.request.urlopen(get_top_news_url) as url:
        get_headlines_data=url.read()
        get_headlines_response=json.loads(get_headlines_data)

        news_results=none

        if get_headlines_response['results']:
            news_results_list=get_headlines_response['results']
            news_results=process_results(news_results_list)

    return news_results

def process_results(news_list):
    """
    function that will process the news results and turn them into objects
    """
    top_news_results=[]
    for item in news_list:
        author=item.get('author')
        title=item.get('title')
        description=item.get('description')
        url=item.get('url')
        urlToImage=item.get('urlToImage')
        published_At=item.get('publishedAt')
        content=item.get('content')

        if urlToImage:
            news_object=Article(author,title,description,url,urlToImage,published_At,content)
            top_news_results.append(news_object)
