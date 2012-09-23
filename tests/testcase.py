import unittest
import os.path as path

class WhoisServersListTestCase(unittest.TestCase):
    
    def readFixtureFileContent(self, file):
        return open(path.dirname(path.realpath(__file__)) + '/fixtures/' + file).read();
