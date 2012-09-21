import unittest
import os.path as path
from whoislist.parser import *

class WhoisServersListParserTest(unittest.TestCase):

    def test_parseWhoisServerUrl_validHtmlPage_mustReturnWhoisServerUrl(self):
        htmlStringToParse = self.readFixtureFileContent('ac.html');
        parser = WhoisServersListParser();
        whoisServerUrl = parser.parseWhoisServerUrl(htmlStringToParse);
        self.assertEqual("whois.nic.ac", whoisServerUrl);

    def readFixtureFileContent(self, file):
        return open(path.dirname(path.realpath(__file__)) + '/fixtures/' + file).read();

    def test_parseWhoisServerUrl_invalidHtmlPage_mustThrowException(self):
        htmlStringToParse = "blablabla";
        parser = WhoisServersListParser();
        self.assertRaises(PatternNotFoundException, parser.parseWhoisServerUrl, htmlStringToParse);

if __name__ == "__main__":
    unittest.main()
