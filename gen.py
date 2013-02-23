#!/usr/bin/python

"""Convert Ben Fry's zip decode database to
GeoJSON and a tab separated file.
"""

import gzip, json
from contextlib import closing

features = []
fields = []

# Read in Ben Fry's database
# Downloaded from http://benfry.com/zipdecode/zips.gz
for l in gzip.open("zips.gz"):
    zipcode = l[0:5]
    lat = float(l[6:16])
    lon = float(l[17:28])

    # Simple data
    fields.append((lon, lat, zipcode))

    # GeoJSON's loquacious feature schema
    features.append({ "type": "Feature",
                      "geometry": {
                        "type": "Point",
                        "coordinates": [lon, lat]
                      },
                      "id": zipcode,
                      "properties": None })

# Emit GeoJSON
collection = { "type": "FeatureCollection",
               "features": features }
with closing(file("zips.geojson", "w")) as fp:
    json.dump(collection, fp)

# Emit TSV file
with closing(file("zips.tsv", "w")) as fp:
    fp.write("lon\tlat\tzip\n")
    for row in fields:
        fp.write("%.3f\t%.3f\t%s\n" % row)
