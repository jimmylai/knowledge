#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Program
'''

import os
import sys
from fabric.api import run, hosts, cd, local, prefix


__author__ = 'noahsark'


def start_solr(solr_main='solr/solr-4.8.0/example', solr_home='%s/solr/conf' % os.getcwd(),
               solr_data='%s/solr/data' % os.getcwd()):
    if os.path.isdir('solr/solr-4.8.0') is False:
        print 'Please download solr-4.8.0 and unzip as solr/solr-4.8.0/'
        return
    with prefix('cd %s' % solr_main):
        local('java -Dsolr.solr.home=%s '
              '-jar start.jar' % (solr_home))
