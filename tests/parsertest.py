import unittest
import os.path as path
from whoislist.parser import *

class WhoisServersListParserTest(unittest.TestCase):

    def test_parseWhoisServerUrl_validHtmlPage_shouldReturnWhoisServerUrl(self):
        htmlStringToParse = self.readFixtureFileContent('ac.html');
        parser = WhoisServersListParser();
        whoisServerUrl = parser.parseWhoisServerUrl(htmlStringToParse);
        self.assertEqual("whois.nic.ac", whoisServerUrl);

    def test_parseWhoisServerUrl_invalidHtmlPage_mustThrowException(self):
        htmlStringToParse = "blablabla";
        parser = WhoisServersListParser();
        self.assertRaises(PatternNotFoundException, parser.parseWhoisServerUrl, htmlStringToParse);

    def test_parseDomainName_validHtmlPage_shouldReturnTopLevelDomainName(self):
        htmlStringToParse = self.readFixtureFileContent('ac.html');
        parser = WhoisServersListParser();
        whoisServerUrl = parser.parseDomainName(htmlStringToParse);
        self.assertEqual("ac", whoisServerUrl);

    def test_parseDomainName_invalidHtmlPage_mustThrowException(self):
        htmlStringToParse = "olololo";
        parser = WhoisServersListParser();
        self.assertRaises(PatternNotFoundException, parser.parseDomainName, htmlStringToParse);

    def test_parseDomainsTable_validHtmlPage_shouldReturnListWithDomains(self):
        htmlToParse = self.readFixtureFileContent('db.html');
        parser = WhoisServersListParser();
        domainsList = parser.parseDomainsTable(htmlToParse);
        self.assertIn({ "domain" : "cc", "link" : "/domains/root/db/cc.html" }, domainsList);

    def test_parseDomainName_invalidHtmlPage_shouldTrowException(self):
        htmlToParse = "trololo";
        parser = WhoisServersListParser();
        self.assertRaises(PatternNotFoundException, parser.parseDomainsTable, htmlToParse);

    def readFixtureFileContent(self, file):
        return open(path.dirname(path.realpath(__file__)) + '/fixtures/' + file).read();

if __name__ == "__main__":
    unittest.main()
