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

    def parseDomainsTable(self, pageContent):
        pattern = re.compile(r'<table id="tld-table".*?</table>', re.DOTALL);
        result = pattern.search(pageContent);
        if not result:
            raise PatternNotFoundException("Table with domains not found");

        domainsTable = result.group();

        pattern = re.compile(r'href="(.*)">(.*)</a>');
        result = pattern.finditer(domainsTable);
        if not result:
            raise PatternNotFoundException("Domains not found in table");

        domains = [];
        
        for domainInfo in result:
            groups = domainInfo.groups();
            domainPage = groups[0];
            domain = groups[1].lower()[1:];
            domains.append({ "domain" : domain, "link" : domainPage });

        return domains;

class PatternNotFoundException(Exception):
    pass;
