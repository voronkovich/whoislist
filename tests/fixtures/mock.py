import os.path as path

class UrlReaderMock:

    def getPageContent(self, url):
        file = url[url.rindex("/") + 1:];
        return open(path.dirname(path.realpath(__file__)) + "/" + file).read();
