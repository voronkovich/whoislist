class WhoisServersListCrawler:

    urlReader = None;
    parser = None;

    url = "";
    baseUrl = "";

    def __init__(self, urlReader, parser, config):
        self.urlReader = urlReader;
        self.parser = parser;
        self.url = config["url"];
        try:
            self.baseUrl = self.url[:self.url.index("/")];
        except ValueError:
            self.baseUrl = self.url;
        print self.baseUrl;
    
    def getWhoisServersList(self):
        whoisServersList = [];
        domains = self.parseDomainsTable();
        whoisServersList = self.parseDomainsPages(domains);
        return whoisServersList;

    def parseDomainsTable(self):
        domainsTable = self.urlReader.getPageContent(self.url);
        return self.parser.parseDomainsTable(domainsTable);

    def parseDomainsPages(self, domains):
        whoisServersList = [];
        for item in domains:
            urlToParse = self.baseUrl + "/" + item["link"];
            domain = self.parseDomainPage(urlToParse);
            whoisServersList.append(domain);
        return whoisServersList;

    def parseDomainPage(self, url):
        pageContent = self.urlReader.getPageContent(url);
        domain = self.parser.parseDomainName(pageContent);
        whois = self.parser.parseWhoisServerUrl(pageContent);
        return { "domain" : domain, "whois" : whois };

class UrlReader:
    pass;
