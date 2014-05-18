from django.shortcuts import render
from django.http import HttpResponse

import pysolr
import json


synonym = pysolr.Solr('http://localhost:8983/solr/synonym_string_match/')
full_text = pysolr.Solr('http://localhost:8983/solr/full_text_search/')


def search(request):
    if 'query' in request.REQUEST:
        query = request.REQUEST['query']
        docs = [i for i in synonym.search('name:%s' % query)]
        if len(docs) > 1:
            docs = docs[:1]
        params = {'rows': '10'}
        if 'location' in request.REQUEST:
            params['fq'] = '+{!geofilt pt=%s sfield=location d=50}' % request.REQUEST['location']
            params['sort'] = 'geodist() asc'
            params['fl'] = 'id,name,abstract,_dist_:geodist()'
            params['sfield'] = 'location'
            params['pt'] = request.REQUEST['location']
        print params
        docs.extend([i for i in full_text.search(query, **params)])
        return HttpResponse(json.dumps(docs))
    return HttpResponse('')


