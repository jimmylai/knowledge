#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Input: redirects_zh.nt.bz2
'''

import re
import json
import bz2
import fileinput


__author__ = 'noahsark'


def get_redirect(string):
    pat = re.compile('"(.*)"@zh')
    match = pat.match(string)
    if match is not None:
        return match.group(1)

items = json.load(open('items.json'))
for line in fileinput.input():
    pat = re.compile("<http://zh.dbpedia.org/resource/(.*)> <http://dbpedia.org/ontology/wikiPageRedirects> <([^<>]*)> .")
    match = pat.match(line)
    if match is not None:
        redirect = match.group(1).decode('unicode_escape')
        uri = match.group(2).decode('unicode_escape')
        if uri in items:
            if 'redirects' not in items[uri]:
                items[uri]['redirects'] = []
            items[uri]['redirects'].append(redirect)

with open('items.json', 'w') as fp:
    fp.write(json.dumps(items, indent=4, ensure_ascii=False).encode('utf8'))
