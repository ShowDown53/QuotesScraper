#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

source = "http://quotes.yourdictionary.com/theme/marriage/"
response = urlopen(source).read()
parse = BeautifulSoup(response)

print "Cheesy " + parse.html.head.title.string.lower() + " just for you:"

citati = parse.findAll("p", attrs={"class": "quoteContent"}, limit=5)

i = 1
for x in citati:
    print str(i) + ". " + x.string.lstrip(' ') # lstrip sem uporabil, ker so določeni citati imeli presledek na začetku
    i += 1

print "Bonus random quote: " + random.choice(citati).string + "\n"

print "Here are some extra random quotes: "
t = 1
for x in random.sample(citati, 5):
    print str(t) + ". " + x.string.lstrip()
    t += 1

