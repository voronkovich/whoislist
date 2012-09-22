class WhoisServersListCrawler:
    _urlReader = None;

    def __init__(self, urlReader, config):
        self._urlReader = urlReader;
        self.config = config;
    
    def getWhoisServersList(self):
        return [];

class UrlReader:
    pass;
