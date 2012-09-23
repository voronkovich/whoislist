from whoislist.crawler import WhoisServersListCrawler, UrlReader
from whoislist.parser import WhoisServersListParser

config = { "url" : "iana.org/domains/root/db" };
crawler = WhoisServersListCrawler(UrlReader(), WhoisServersListParser(), config);
whoisServersList = crawler.getWhoisServersList();
