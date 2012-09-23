def convertToXml(whoisServersList):
    result = [];
    result.append('<?xml version="1.0"?>\n<whoisServers>');

    for server in whoisServersList:
    result.write('<server zone="' + server["domain"] + '" url="' + server["whois"] + '" />');

    result.append('</whoisServers>');
    return result.join('\n');

def convertToPlainText(whoisServersList, delimeter = ": "):
    result = [];

    for server in whoisServersList:
        outputFile.append(server["domain"] + delimeter + server["whois"]);

    return result.join('\n');
