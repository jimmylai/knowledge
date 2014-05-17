#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Program
'''

import sys
import json


__author__ = 'noahsark'

relations = set()

items = json.load(open('items.json'))
for key, val in items.iteritems():
    if 'relations' in val:
        for rel in val['relations']:
            relations.add(rel)

print len(relations)
print relations
