#! /usr/bin/env python3
from isilon import Isilon

# The Isilon class sets up the connection to the Isilon and provides an object
i = Isilon(api_class="StatisticsApi")

response = i.call_method(method='get_summary_system', nodes='1,2,3,4')

for measurement in response.system:
    measure = "cpu"
    tags = f"nodes={measurement.node}"
    fields = f"cpu={measurement.cpu}"
    print(f"{measure},{tags} {fields}")
