#!/usr/bin/env python

import swat
import os

cashost = 'sas-cas-server-default-client'
casport = 5570
passwordToken = os.environ.get('ACCESS_TOKEN')

conn = swat.CAS(hostname=cashost, port=casport, password=passwordToken)

display(conn)
print(conn.serverstatus())
type(conn)
conn.about()['About']['Viya Version']

conn.fileInfo(caslib = 'casuser')

import pandas as pd
import numpy as np

conn.read_csv('data/courses/CASL/data/my_data/cars.csv', casout={'name':'cars', 'caslib':'casuser', 'replace':True})

conn.fileInfo(caslib = 'casuser')

castbl = conn.CASTable('cars', caslib = 'casuser')

display(type(castbl), castbl)

castbl.tableDetails()

df = castbl.head()

display(df)

conn.close()


