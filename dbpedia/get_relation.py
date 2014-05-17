#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Input: raw_infobox_properties_en.nt.bz2
'''

import re
import json
import bz2
import fileinput


__author__ = 'noahsark'


def get_latlon(string):
    pat = re.compile('"(.*) (.*)"@en')
    match = pat.match(string)
    if match is not None:
        return "%lf,%lf" % (float(match.group(1)), float(match.group(2)))

def get_relation(string):
    pat = re.compile('http://dbpedia.org/property/(.*)')
    match = pat.match(string)
    if match is not None:
        return match.group(1)

def get_entity(string):
    pat = re.compile('http://dbpedia.org/resource/.*')
    match = pat.match(string)
    if match is not None:
        return string

items = json.load(open('entities.json'))
id_list = set(json.load(open('id_list.json')))
for line in fileinput.input():
    pat = re.compile("<([^<>]*)> <([^<>]*)> <([^<>]*)> .")
    match = pat.match(line)
    if match is not None and get_entity(match.group(3)) is not None:
        uri = match.group(1).decode('unicode_escape')
        relation = get_relation(match.group(2)).decode('unicode_escape')
        entity = get_entity(match.group(3)).decode('unicode_escape')
        if uri not in id_list:
            continue
        if uri not in items:
            items[uri] = {}
        if 'relations' not in items[uri]:
            items[uri]['relations'] = {}
        items[uri]['relations'][relation] = entity

with open('entities.json', 'w') as fp:
    fp.write(json.dumps(items, indent=4, ensure_ascii=False).encode('utf8'))
