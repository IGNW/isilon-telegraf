#! /usr/bin/env python3
from isilon import Isilon

# The Isilon class sets up the connection to the Isilon and provides an object
i = Isilon(api_class="StoragepoolApi")

response = i.call_method(method='get_storagepool_nodepool', storagepool_nodepool_id='v200_100gb_6gb')

for node in response.nodepools:
    measure = "node_pool"
    tags = f"name={node.name},tier={node.tier}"
    fields = f"percent_used={node.usage.pct_used}"
    print(f"{measure},{tags} {fields}")
