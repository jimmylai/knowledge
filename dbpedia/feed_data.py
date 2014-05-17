#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Program
'''

import re
import sys
import json
from fabric.api import run, hosts, cd, local, prefix
from util import *


__author__ = 'noahsark'


if len(sys.argv) < 2:
    print 'please specify geed type as parameter'
    sys.exit(0)


def feed_string_match(core, extract):
    results = []
    for key, val in items.iteritems():
        dic = extract(key, val)
        results.append(dic)

    fpath = '%s_feed.json' % core
    with open(fpath, 'w') as fp:
        fp.write(json.dumps(results, indent=4, ensure_ascii=False).encode('utf8'))

    clear_data(core)
    feed_data(core, fpath)


items = json.load(open('entities.json'))
if sys.argv[1] == 'string_match':
    feed_string_match('string_match',
            lambda key, val: {'id': key, 'name': get_name(key), 'abstract': val['abstract'] if 'abstract' in val else ''})


if sys.argv[1] == 'synonym_string_match':
    results = []
    for key, val in items.iteritems():
        name = get_name(key)
        if 'redirects' in val:
            line ='%s => %s\n' % (', '.join([i.replace('_', ' ').replace(',', '\\,') for i in val['redirects']]), name) 
            results.append(line.encode('utf8'))

    with open('../solr/conf/synonym_string_match/conf/synonyms.txt', 'w') as fp:
        fp.writelines(results)
    feed_string_match('synonym_string_match',
            lambda key, val: {'id': key, 'name': get_name(key), 'abstract': val['abstract'] if 'abstract' in val else ''})

if sys.argv[1] == 'geo_search':
    feed_string_match('geo_search',
            lambda key, val: {'id': key, 'name': get_name(key), 'abstract': val['abstract'] if 'abstract' in val else None,
                'location': val['latlon'] if 'latlon' in val else None})
