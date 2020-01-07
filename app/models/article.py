class Article:
    """
    article class to define  the article objects
    """
    def __init__(self,author,title,description,url,urlToImage,published_At,content):
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.published_At=published_At
        self.content=content