import unittest
from testcase import WhoisServersListTestCase
from whoislist.converter import *

class ConverterTest(WhoisServersListTestCase):

    def setUp(self):
        self.whoisDomainsList = [
            { "domain" : "ac", "whois": "whois.nic.ac" },
            { "domain" : "br", "whois": "whois.registro.br" },
        ];

    def test_convertToXml_ValidData_shouldReturnXmlString(self):
        result = convertToXml(self.whoisDomainsList);
        result = self.deleteExtraCharacters(result);
        expectedResult = self.readFixtureFileContent('whois-servers.xml');
        expectedResult = self.deleteExtraCharacters(expectedResult);
        self.assertEqual(expectedResult, result);

    def test_convertToPlainText_ValidData_shouldReturnPlainTextString(self):
        result = convertToPlainText(self.whoisDomainsList);
        result = self.deleteExtraCharacters(result);
        expectedResult = self.readFixtureFileContent('whois-servers.txt');
        expectedResult = self.deleteExtraCharacters(expectedResult);
        self.assertEqual(expectedResult, result);

    def deleteExtraCharacters(self, str):
        return str.translate(None, '\r\n\t');
         
if __name__ == "__main__":
    unittest.main()
