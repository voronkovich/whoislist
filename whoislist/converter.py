import string

def convertToXml(whoisServersList):
    result = [];
    result.append('<?xml version="1.0"?>\n<whoisServers>');

    for server in whoisServersList:
        result.append('<server zone="' + server["domain"] + '" url="' + server["whois"] + '" />');

    result.append('</whoisServers>');
    return string.join(result, "\n");

def convertToPlainText(whoisServersList, delimeter = ": "):
    result = [];

    for server in whoisServersList:
        result.append(server["domain"] + delimeter + server["whois"]);

    return string.join(result, '\n');
