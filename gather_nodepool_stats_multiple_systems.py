#! /usr/bin/env python3
from isilon import Isilon

# The Isilon class sets up the connection to the Isilon and provides an object
node_1 = Isilon(api_class="StoragepoolApi", settings_file='node_1_settings.yml')
node_2 = Isilon(api_class="StoragepoolApi", settings_file='node_2_settings.yml')
node_3 = Isilon(api_class="StoragepoolApi", settings_file='node_3_settings.yml')
node_4 = Isilon(api_class="StoragepoolApi", settings_file='node_4_settings.yml')

responses = []
responses.append(node_1.call_method(method='get_storagepool_nodepool', storagepool_nodepool_id='v200_100gb_6gb'))
responses.append(node_2.call_method(method='get_storagepool_nodepool', storagepool_nodepool_id='v200_100gb_6gb'))
responses.append(node_3.call_method(method='get_storagepool_nodepool', storagepool_nodepool_id='v200_100gb_6gb'))
responses.append(node_4.call_method(method='get_storagepool_nodepool', storagepool_nodepool_id='v200_100gb_6gb'))

for response in responses:
    for node in response.nodepools:
        measure = "node_pool"
        tags = f"name={node.name},tier={node.tier}"
        fields = f"percent_used={node.usage.pct_used}"
        print(f"{measure},{tags} {fields}")
