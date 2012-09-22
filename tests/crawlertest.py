import unittest
import os.path as path
from fixtures.mock import UrlReader
from whoislist.crawler import *

class WhoisServersListCrawlerTest(unittest.TestCase):

    def setUp(self):
        self.crawler = WhoisServersListCrawler();

    def test_getWhoisServersList_commonUse_sholdReturnListWithWhoisServers(self):
        whoisList = self.crawler.getWhoisServersList();
        self.assertIn({ "domain" : "br", "whois": "whois.registro.br" }, whoisList);

if __name__ == "__main__":
    unittest.main()
