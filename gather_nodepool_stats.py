#! /usr/bin/env python3
import urllib3
import os

import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from settings import Settings

urllib3.disable_warnings()

config = Settings()

# configure cluster connection: basicAuth
url = f"https://{config.hostname}:{config.port}"
configuration = isi_sdk_8_2_1.Configuration()
configuration.host = url 
configuration.username = config.username 
configuration.password = config.password 
configuration.verify_ssl = config.verify_ssl

# create an instance of the API class
api_client = isi_sdk_8_2_1.ApiClient(configuration)
storage_instance = isi_sdk_8_2_1.StoragepoolApi(api_client)

try:
    api_response = storage_instance.get_storagepool_nodepool('v200_100gb_6gb')
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_nfs_exports: %s\n" % e)

for node in api_response.nodepools:
    measure = "node_pool"
    tags = f"name={node.name},tier={node.tier}"
    fields = f"percent_used={node.usage.pct_used}"
    print(f"{measure},{tags} {fields}")
