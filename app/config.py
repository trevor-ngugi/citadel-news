class Config:
    '''
    General configuration parent class
    '''
    TOP_NEWS_URL='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_SOURCES_URL='https://newsapi.org/v2/sources?apiKey={}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True