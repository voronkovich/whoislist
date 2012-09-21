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

class PatternNotFoundException(Exception):
    pass;
