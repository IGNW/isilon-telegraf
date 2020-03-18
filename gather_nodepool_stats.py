#! /usr/bin/env python3
import urllib3
import os
from dotenv import load_dotenv
from pprint import pprint

import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException

urllib3.disable_warnings()
load_dotenv()

# configure cluster connection: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.host = 'https://10.50.4.53:8080'
configuration.username = os.environ['username']
configuration.password = os.environ['password']
configuration.verify_ssl = False

# create an instance of the API class
api_client = isi_sdk_8_2_1.ApiClient(configuration)
storage_instance = isi_sdk_8_2_1.StoragepoolApi(api_client)
stats_instance = isi_sdk_8_2_1.StatisticsApi(api_client)
protocols_instance = isi_sdk_8_2_1.ProtocolsApi(api_client)

try:
    api_response = storage_instance.get_storagepool_nodepool('v200_100gb_6gb')
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_nfs_exports: %s\n" % e)

for node in api_response.nodepools:
    measure = "node_pool"
    tags = f"name={node.name},tier={node.tier}"
    fields = f"percent_used={node.usage.pct_used}"
    print(f"{measure},{tags} {fields}")
