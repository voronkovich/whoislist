whoislist
=========

Utility for parsing whois-servers from http://www.iana.org/domains/root/db.

Usage:

    getwhoislist.py [-h] [--xml] file

positional arguments:
    file        Set the file name where the results will be written

    optional arguments:
        -h, --help  show this help message and exit
        --xml       Set the output format to XML

Example:

    getwhoislist --xml whois.xml

Or:

    getwhoislist whois.txt
