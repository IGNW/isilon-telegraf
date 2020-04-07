#! /usr/bin/env python3
from isilon import Isilon
import argparse

# Read in stat from the command line
parser = argparse.ArgumentParser()
parser.add_argument("statistic", help="Display Statistics Key Details.  Example: cluster.node.list.all")
args = parser.parse_args()

# The Isilon class sets up the connection to the Isilon and provides an object
s = Isilon(api_class="StatisticsApi")

# Sample of the name of the stat
# stat_key = 'node.clientstats.proto.nfs'

stat_key = args.statistic

response = s.call_method(method='get_statistics_key', statistics_key_id=stat_key)
print('\n*********************\n')
print("Structure details of the key")
print(response)
print('\n*********************\n')

print("Data in the key from the API\n")
response = s.call_method(method='get_statistics_current', key=stat_key, devid='all')
print(response)
