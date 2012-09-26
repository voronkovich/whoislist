#!/usr/bin/python

from whoislist.crawler import WhoisServersListCrawler, UrlReader
from whoislist.parser import WhoisServersListParser
from whoislist.converter import *
from argparse import ArgumentParser

argsParser = ArgumentParser(description = "Parse WHOIS-servers list from http://www.iana.org/domains/root/db.");
argsParser.add_argument("file", help="Set the file name where the results will be written");
argsParser.add_argument("--xml", help="Set the output format to XML", action="store_true");
args = argsParser.parse_args();

config = { "url" : "http://www.iana.org/domains/root/db" };
crawler = WhoisServersListCrawler(UrlReader(), WhoisServersListParser(), config);
whoisServersList = crawler.getWhoisServersList();

file = open(args.file, "w");
if (args.xml):
    output = convertToXml(whoisServersList);
else:
    output = convertToPlainText(whoisServersList);

file.write(output);
file.close();
