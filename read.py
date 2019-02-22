#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import re
import config
import os
import isnumber

with open('quotes.json') as f:
    data = json.loads(f.read())
    i = 0
    for content in data:
        if not isnumber.is_number(str(content['sorted'])):
            content['sorted'] = len(data) - i
            i = i + 1
    try:
        data.sort(key = lambda x:int(x["sorted"]))
        fw = open('result/'+config.save_name, 'w') 
        for content in data:
            fw.write(content['title'])
            fw.write(content['text'][0].replace('<div id="content">','').
                replace('<script>chaptererror();</script>','').
                replace('</div>','').replace('<br>　　<br>','\n'))
            print(content['title'])
            print(content['text'][0].replace('<div id="content">','').
                replace('<script>chaptererror();</script>','').
                replace('</div>','').replace('<br>　　<br>','\n'))
    except Exception as e:
        raise e

    w = open('quotes.json','w')
    w.truncate()
    w.close()
    fw.close()
