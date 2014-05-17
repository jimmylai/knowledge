#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Input: redirects_en.nt.bz2
'''

import re
import json
import bz2
import fileinput


__author__ = 'noahsark'


items = json.load(open('entities.json'))
for line in fileinput.input():
    pat = re.compile("<http://dbpedia.org/resource/(.*)> <http://dbpedia.org/ontology/wikiPageRedirects> <([^<>]*)> .")
    match = pat.match(line)
    if match is not None:
        redirect = match.group(1).decode('unicode_escape')
        uri = match.group(2).decode('unicode_escape')
        if uri not in items:
            items[uri] = {}

        if 'redirects' not in items[uri]:
            items[uri]['redirects'] = []
        items[uri]['redirects'].append(redirect)

with open('entities.json', 'w') as fp:
    fp.write(json.dumps(items, indent=4, ensure_ascii=False).encode('utf8'))
