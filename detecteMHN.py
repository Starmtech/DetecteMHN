#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import httplib
import socket
import ssl

class Detectionmhn:

    def __init__(self, url):
        self.url = "starmtech.fr"
        self.status = "false"
        self.code = "404"

    def Getstatus(self):
        print "le status vos:", self.status

    def CheckURL(self):
        useragent = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        req = "/api/script/?text=true&script_id=1"
        try:
            conn = httplib.HTTPSConnection(self.url, context=ssl._create_unverified_context())
            conn.request("HEAD", req, headers = useragent)
        except socket.error:
            conn = httplib.HTTPConnection(self.url, 80)
            conn.request("HEAD", req, headers = useragent)
        reponse = conn.getresponse()
        print reponse.status, reponse.reason
        if reponse.status == 200:
            self.status = "false"
            data = reponse.read()
            print data
            print "Le serveur est un honeypot (MHN)"
        else:
            self.status = "true"
            print "le serveur n'est pas un honeypot (MHN)"

if __name__ == '__main__':
        if len(sys.argv) > 1 :
            url = sys.argv[1]
        else:
            url = raw_input("Indiquer une URL. ")
        test = Detectionmhn(url)
        test.CheckURL()
        sys.exit (1)
