import unittest
import os.path as path
from whoislist.parser import WhoisServersListParser

class WhoisServersListParserTest(unittest.TestCase):

    def test_parseWhoisServerUrl_returnWhoisServerUrl(self):
        htmlStringToParse = self.readFixtureFileContent('ac.html');
        parser = WhoisServersListParser();
        whoisServerUrl = parser.parseWhoisServerUrl(htmlStringToParse);
        self.assertEqual("whois.nic.ac", whoisServerUrl);

    def readFixtureFileContent(self, file):
        return open(path.dirname(path.realpath(__file__)) + '/fixtures/' + file).read();

if __name__ == "__main__":
    unittest.main()
