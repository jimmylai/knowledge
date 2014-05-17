#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Input: short_abstracts_en.nt.bz2
'''

import re
import json
import bz2
import fileinput


__author__ = 'noahsark'


types = set(['Place'])

results = []
for line in fileinput.input():
    pat = re.compile("<([^<>]*)> <([^<>]*)> <http://dbpedia.org/ontology/(.*)> .")
    match = pat.match(line)
    if match is not None:
        if match.group(3) in types:
            uri = match.group(1).decode('unicode_escape')
            results.append(uri)

with open('id_list.json', 'w') as fp:
    fp.write(json.dumps(results, indent=4, ensure_ascii=False).encode('utf8'))
