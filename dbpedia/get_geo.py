#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Input: geo_coordinates_zh.nt.bz2
'''

import re
import json
import bz2
import fileinput


__author__ = 'noahsark'


def get_latlon(string):
    pat = re.compile('"(.*) (.*)"@zh')
    match = pat.match(string)
    if match is not None:
        return "%lf,%lf" % (float(match.group(1)), float(match.group(2)))

items = json.loads(open('items.json'))
for line in fileinput.input():
    pat = re.compile("<([^<>]*)> <([^<>]*)> (.*) .")
    match = pat.match(line)
    if match is not None:
        if match.group(2) == 'http://www.georss.org/georss/point':
            uri = match.group(1).decode('unicode_escape')
            if uri not in items:
                items[uri] = {}
            items[uri]['latlon'] = get_latlon(match.group(3))

with open('items.json', 'w') as fp:
    fp.write(json.dumps(items, indent=4, ensure_ascii=False).encode('utf8'))
