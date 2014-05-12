#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Program
'''

import re
import json
import bz2
import fileinput


__author__ = 'noahsark'


def get_abstract(string):
    pat = re.compile('"(.*)"@zh')
    match = pat.match(string)
    if match is not None:
        return match.group(1)

items = json.load(open('items.json'))
for line in fileinput.input():
    pat = re.compile("<([^<>]*)> <([^<>]*)> (.*) .")
    match = pat.match(line)
    if match is not None:
        if match.group(2) == 'http://www.w3.org/2000/01/rdf-schema#comment':
            uri = match.group(1).decode('unicode_escape')
            if uri not in items:
                items[uri] = {}
            items[uri]['abstract'] = get_abstract(match.group(3)).decode('unicode_escape')

with open('items.json', 'w') as fp:
    fp.write(json.dumps(items, indent=4, ensure_ascii=False).encode('utf8'))
