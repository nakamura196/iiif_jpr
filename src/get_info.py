import pandas as pd
from rdflib import URIRef, BNode, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF, XSD
from rdflib import Namespace
import numpy as np
import math
import sys
import argparse
import json
import glob
import os
import urllib.request

import csv

f = open('data/manifests.csv', 'r')

rows = []
rows.append(["manifest", "Exist", "Thumbnail", "Attribution", "License"])

reader = csv.reader(f)
header = next(reader)

count = 0

for row in reader:

    count += 1

    manifest = row[0]

    print(count)
    print(manifest)

    attr = ""
    license = ""
    th = ""

    try:
        res = urllib.request.urlopen(manifest)
        data = json.loads(res.read())
        th = data["sequences"][0]["canvases"][0]["images"][0]["resource"]["service"]["@id"] + \
            "/full/200,/0/default.jpg"

        if "attribution" in data:
            attr = data["attribution"]

        if "license" in data:
            license = data["license"]

        exist = 1

    except:

        exist = 0

    rows.append([manifest, exist, th, attr, license])


f.close()

f = open('data/result.csv', 'w')

writer = csv.writer(f, lineterminator='\n')
writer.writerows(rows)

f.close()
