import re;

class WhoisServersListParser:

    def parseWhoisServerUrl(self, pageContent):
        pattern = re.compile(r'<b>WHOIS Server:</b>(.*?)</p>', re.DOTALL);
        result = pattern.search(pageContent);
        if (result):
            whois = result.groups()[0].strip();
            return whois;
        else:
            raise PatternNotFoundException("Whois server url not found");

    def parseDomainName(self, pageContent):
        pattern = re.compile(r'<h1>Delegation Record for \.(.*?)</h1>', re.DOTALL);
        result = pattern.search(pageContent);
        if (result):
            domain = result.groups()[0].strip().lower();
            return domain;
        else:
            raise PatternNotFoundException("Whois server url not found");

class PatternNotFoundException(Exception):
    pass;
