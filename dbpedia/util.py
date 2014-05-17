#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Program
'''

import re
from fabric.api import run, hosts, cd, local, prefix


__author__ = 'noahsark'


def get_name(string):
    pat = re.compile("http://zh.dbpedia.org/resource/(.*)")
    match = pat.match(string)
    if match is not None:
        return match.group(1)

def clear_data(core):
    local('curl "http://localhost:8983/solr/%s/update?stream.body=<delete><query>*:*</query></delete>&commit=true"' % core)


def feed_data(core, fpath):
    url = 'http://localhost:8983/solr/%s/update' % core
    local("curl %s/json?commit=true --data-binary @%s -i -H 'Content-type:application/json'" % (
            url, fpath))
    local("curl %s?softCommit=true -i" % (url))
