#! /usr/bin/env python3
import urllib3
import os

import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from settings import Settings

urllib3.disable_warnings()

config = Settings()

print(config.hostname)
print(config.username)
print(config.password)

url = f"https://{config.hostname}:{config.port}"
print(url)
configuration = isi_sdk_8_2_1.Configuration()
configuration.host = url 
configuration.username = config.username 
configuration.password = config.password 
configuration.verify_ssl = False

# create an instance of the API class
api_client = isi_sdk_8_2_1.ApiClient(configuration)
statistics_instance = isi_sdk_8_2_1.StatisticsApi(api_client)

try:
    api_response = statistics_instance.get_summary_system(nodes='1,2,3,4')
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_nfs_exports: %s\n" % e)

for measurement in api_response.system:
    measure = "cpu"
    tags = f"nodes={measurement.node}"
    fields = f"cpu={measurement.cpu}"
    print(f"{measure},{tags} {fields}")
