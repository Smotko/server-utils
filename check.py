#!/usr/bin/python

import requests

import socket

def checkWebsites():
    print "Checking websites"
    sites = ['http://psywerx.net', 'http://gitlab.psywerx.net', 'http://stejem.psywerx.net/',
             'http://vodim.si', 'http://slabefotke.com', 'http://slabescene.com/', 
             'http://siviljstvo-alenka.com', 'http://vezenje-kranj.com', 'http://maleficusangelus.com',
             'http://mavricnistumfki.net']

    for s in sites:
        try:
            r = requests.get(s)
            if r.status_code != 200:
                print s, "returned", r.status_code
        except requests.exceptions.ConnectionError:
                print s, "connection error"

def checkServices():
    print "Checking services"
    
    services = [
        ('smotko ssh', 'zidar.me', 11022),
        ('mail', 'mail.psywerx.net', 25),
        ('minecraft ssh', 'zidar.me', 12022),
        ('minecraft', 'minecraft.psywerx.net', 25565),
        
    ]

    for name, address, port in services:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((address, port))
        if(result != 0):
            print name, "seems to be down"    
    
    

if __name__ == "__main__":
    checkWebsites()
    checkServices()