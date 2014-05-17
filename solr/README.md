Solr
====
Download Solr from: http://www.apache.org/dyn/closer.cgi/lucene/solr/4.8.0
And extract to solr/solr-4.8.0




Synonym String Match
====================
Reference:
https://cwiki.apache.org/confluence/display/solr/Understanding+Analyzers,+Tokenizers,+and+Filters

Example query:


GEO Search
==========
Reference:
https://cwiki.apache.org/confluence/display/solr/Spatial+Search

Example query:
http://localhost:8983/solr/geo_search/select?q=*%3A*&fq=%7B!geofilt%7D&sort=geodist()+asc&fl=id%2Cname%2Cabstract%2Clocation%2C_dist_%3Ageodist()&wt=json&indent=true&spatial=true&pt=25.034731%2C121.521934&sfield=location&d=2

