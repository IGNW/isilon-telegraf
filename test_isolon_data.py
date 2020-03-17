from pprint import pprint
import time
import urllib3
import os

import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException

urllib3.disable_warnings()

# configure cluster connection: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.host = 'https://10.50.4.53:8080'
configuration.username = os.environ['username'] 
configuration.password = os.environ['password'] 
configuration.verify_ssl = False

# create an instance of the API class
api_client = isi_sdk_8_2_1.ApiClient(configuration)
api_instance = isi_sdk_8_2_1.ProtocolsApi(api_client)


# get all exports
sort = 'description'
limit = 50
direction = 'ASC'
try:
    api_response = api_instance.list_nfs_exports(sort=sort, limit=limit, dir=direction)
    #pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_nfs_exports: %s\n" % e)

try:
    api_response = api_instance.get_ftp_settings()
    pprint(api_response)
    print(dir(api_response))
    resp = api_response.to_dict()
    print(resp['settings'])
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_nfs_exports: %s\n" % e)

