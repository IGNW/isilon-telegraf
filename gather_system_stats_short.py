#! /usr/bin/env python3
from isilon import Isilon, ApiException

# The Isilon class sets up the connection to the Isilon and provides an object
api = Isilon(api_class="StatisticsApi")
api_instance = api.api_client

try:
    api_response = api_instance.get_summary_system(nodes='1,2,3,4')
except ApiException as e:
    print("Exception when calling Statistics Api: %s\n" % e)

for measurement in api_response.system:
    measure = "cpu"
    tags = f"nodes={measurement.node}"
    fields = f"cpu={measurement.cpu}"
    print(f"{measure},{tags} {fields}")
