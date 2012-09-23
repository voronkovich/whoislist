from whoislist.crawler import WhoisServersListCrawler, UrlReader
from whoislist.parser import WhoisServersListParser

config = { "url" : "http://www.iana.org/domains/root/db" };
crawler = WhoisServersListCrawler(UrlReader(), WhoisServersListParser(), config);
whoisServersList = crawler.getWhoisServersList();
saveResultsToFile("whois-servers.xml");

def saveResultsToFile(fileName, domains):
    outputFile = open(fileName, "w");
    outputFile.write('<?xml version="1.0"?>\n');
    outputFile.write('<servers>\n');

    for domain in domains:
        outputFile.write('<server zone="' + domain["domain"] + '" url="' + domain["whois"] + '" />\n');
        
    outputFile.write('</servers>');
    outputFile.close();
    return;

def saveResultsToTextFile(fileName, domains):
    outputFile = open(fileName, "w");

    for domain in domains:
        outputFile.write(domain["domain"] + ': ' + domain["whois"] + '\n');
        
    outputFile.close();
    return;
