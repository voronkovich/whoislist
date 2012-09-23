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
        result = result.translate(None, '\r\n\t');
        expectedResult = self.readFixtureFileContent('whois-servers.xml');
        expectedResult = expectedResult.translate(None, '\r\n\t');
        self.assertEqual(expectedResult, result);
         
if __name__ == "__main__":
    unittest.main()
