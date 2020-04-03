#! /usr/bin/env python3
from isilon import Isilon
import csv

# The Isilon class sets up the connection to the Isilon and provides an object
s = Isilon(api_class="StatisticsApi")

# Get all 5000+ stats from the system
response = s.call_method(method='get_statistics_keys')

# Put the key and the description into a list of dicts
output = []
for resp in response.keys:
    output.append({'key': resp.key, 'description': resp.description})

# write the output to a CSV file
# if you commit to a github repo, github renders it nicely
# adds searching, etc
with open("nfs_stats.csv", 'w') as f:
    field_names = ['key', 'description']
    writer = csv.DictWriter(f, fieldnames=field_names)

    writer.writeheader()
    for o in output:
        writer.writerow(o)
