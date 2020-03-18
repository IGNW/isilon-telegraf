#! /usr/bin/env python3
import urllib3
import os
from dotenv import load_dotenv

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
statistics_instance = isi_sdk_8_2_1.StatisticsApi(api_client)

try:
    api_response = statistics_instance.get_summary_drive()
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_nfs_exports: %s\n" % e)

for drive in api_response.drive:
    if drive.type != "UNKNOWN":
        measure = "drive"
        tags = f"drive_id={drive.drive_id},type={drive.type}"
        fields = f"percent_used={drive.used_bytes_percent}"
        print(f"{measure},{tags} {fields}")
