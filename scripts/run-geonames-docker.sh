#!/bin/bash
docker pull elasticsearch:5.5.2
docker run -d -p 127.0.0.1:9200:9200 -v $(pwd)/../geonames_index/:/usr/share/elasticsearch/data elasticsearch:5.5.2
