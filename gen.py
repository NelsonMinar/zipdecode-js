#!/usr/bin/python

import gzip, json
from contextlib import closing

features = []
fields = []

for l in gzip.open("zips.gz"):
    zipcode = l[0:5]
    lat = float(l[6:16])
    lon = float(l[17:28])
    fields.append((lon, lat, zipcode))
    features.append({ "type": "Feature",
                      "geometry": {
                        "type": "Point",
                        "coordinates": [lon, lat]
                      },
                      "id": zipcode,
                      "properties": None })

collection = { "type": "FeatureCollection",
               "features": features[:2] }
with closing(file("zips.geojson", "w")) as fp:
    json.dump(collection, fp)
with closing(file("zips.tsv", "w")) as fp:
    fp.write("lon\tlat\tzip\n")
    for row in fields:
        fp.write("%.3f\t%.3f\t%s\n" % row)
