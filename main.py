#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

source = "http://quotes.yourdictionary.com/theme/marriage/"
response = urlopen(source).read()
parse = BeautifulSoup(response)

print "Cheesy " + parse.html.head.title.string.lower() + " just for you:"

citati = parse.findAll("p", attrs={"class": "quoteContent"})

i = 1
for x in citati:
    if i <= 5:
        print str(i) + ". " + x.string.lstrip(' ') # lstrip sem uporabil, ker so določeni citati imeli presledek na začetku
        i += 1
    else:
        break

print "Bonus random quote: " + random.choice(citati).string + "\n"

print "Here are some extra random quotes: "
t = 1
for x in citati:
    if t <= 5:
        print str(t) + ". " + random.choice(citati).string.lstrip(' ')
        t += 1
    else:
        break
