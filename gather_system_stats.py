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
protocol_instance = isi_sdk_8_2_1.ProtocolsApi(api_client)
sync_instance = isi_sdk_8_2_1.SyncApi(api_client)
cluster_instance = isi_sdk_8_2_1.ClusterApi(api_client)
statistics_instance = isi_sdk_8_2_1.StatisticsApi(api_client)

# get all exports
# sort = 'description'
# limit = 50
# direction = 'ASC'
# try:
#     api_response = api_instance.list_nfs_exports(sort=sort, limit=limit, dir=direction)
#     #pprint(api_response)
# except ApiException as e:
#     print("Exception when calling ProtocolsApi->list_nfs_exports: %s\n" % e)

try:
    api_response = statistics_instance.get_summary_system(nodes='1,2,3,4')
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_nfs_exports: %s\n" % e)

#pprint(api_response)
#print(dir(api_response))
#print(api_response.system)
def disp_var(text=None, var=None):
    print(f'{text}: {var}')

disp_var("cpu", api_response.system[0].cpu)
disp_var("cpu", api_response)
# disp_var("cpu", api_response.system[1].cpu)
# disp_var("cpu", api_response.system[2].cpu)
# disp_var("cpu", api_response.system[3].cpu)
# disp_var("http", api_response.system[0].http)
# disp_var("ftp", api_response.system[0].ftp)
# disp_var("total", api_response.system[0].total)
disp_var("time", api_response.system[0].time)
