#!/bin/bash

curl -G "http://overpass-api.de/api/interpreter" --data-urlencode data@stadt-abfrage.txt | tail -n +2 | sort | uniq > stadt.txt
curl -G "http://overpass-api.de/api/interpreter" --data-urlencode data@land-abfrage.txt | tail -n +2 | sort | uniq > land.txt
curl -G "http://overpass-api.de/api/interpreter" --data-urlencode data@fluss-abfrage.txt | tail -n +2 | sort | uniq > fluss.txt
