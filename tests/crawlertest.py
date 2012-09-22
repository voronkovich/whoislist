import unittest
import os.path as path
from whoislist.crawler import *

class WhoisServersListCrawlerTest(unittest.TestCase):

    def test_start_commonUse_shouldReturnArray(self):
        crawler = WhoisServersListCrawler();
        whoisList = crawler.start();
        self.assertIsInstance(whoisList, list);        

if __name__ == "__main__":
    unittest.main()
