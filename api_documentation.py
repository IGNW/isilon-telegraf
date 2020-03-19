#! /usr/bin/env python3
import urllib3
import os
from dotenv import load_dotenv
from pprint import pprint

# The main repo for the library is here:
# https://github.com/Isilon/isilon_sdk

# The Documentation for the version of Isolon is here:
# https://github.com/Isilon/isilon_sdk_python
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException

# This disables the insecure https warnings we'll get
# because the Virtual Isolon does not have a proper HTTPS cert
urllib3.disable_warnings()

# This is how the settings in the .env file are getting loaded
# Specifically this is where the username and password
# are getting loaded at run time into environmental variables
#
# https://pypi.org/project/python-dotenv/
load_dotenv()

# configure cluster connection: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.host = 'https://10.50.4.53:8080'
configuration.username = os.environ['username']
configuration.password = os.environ['password']
configuration.verify_ssl = False

# Pass all the configurations into the API
api_client = isi_sdk_8_2_1.ApiClient(configuration)

# Create the callable objects for each of the API Categories
# Below is an example of 3 of the categories
# There are about 20 categories of API's

# https://github.com/Isilon/isilon_sdk_python
# On the link above, clicking on any of the methods like
# get_summary_drive at 
# https://github.com/Isilon/isilon_sdk_python/blob/v8.2.1/docs/StatisticsApi.md#get_summary_drive
# This will give you a code snipit of the above code
# and a working example
protocols_instance = isi_sdk_8_2_1.ProtocolsApi(api_client)
stats_instance = isi_sdk_8_2_1.StatisticsApi(api_client)
storage_instance = isi_sdk_8_2_1.StoragepoolApi(api_client)

# The below is an example of calling the get_storagepool_nodepool api
# Using the StoreagepoolApi
try:
    api_response = storage_instance.get_storagepool_nodepool('v200_100gb_6gb')
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_nfs_exports: %s\n" % e)

# This is the loop that parses the desired data from the response
# And puts the output into the Influx format for parsing by telegraf
for node in api_response.nodepools:
    measure = "node_pool"
    tags = f"name={node.name},tier={node.tier}"
    fields = f"percent_used={node.usage.pct_used}"
    print(f"{measure},{tags} {fields}")


