#!/bin/bash

set -eu

TS=`date +%s`
DATE=`date`
git tag -a deploy-$TS -m "Deploy at $DATE"
rsync -av \
  index.html queue.min.js us-states.geojson zips.tsv \
  somebits.com:/var/www/zipdecode-js/
