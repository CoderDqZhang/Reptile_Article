#!/usr/bin/env python
# -*- coding:utf-8 -*-



import os
import article_biquge

cmd = 'scrapy runspider article_biquge.py -o quotes.json'
textlist = os.popen(cmd).readlines()
for line in textlist:
	print(line)

save = 'python3 read.py'
textlist = os.popen(save).readlines()
for line in textlist:
	print(line)

