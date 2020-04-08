#! /usr/bin/env python3
from isilon import Isilon

# The Isilon class sets up the connection to the Isilon and provides an object
nodes = []
nodes.append(Isilon(api_class="StoragepoolApi", settings_file='node_1_settings.yml'))
nodes.append(Isilon(api_class="StoragepoolApi", settings_file='node_2_settings.yml'))
nodes.append(Isilon(api_class="StoragepoolApi", settings_file='node_3_settings.yml'))
nodes.append(Isilon(api_class="StoragepoolApi", settings_file='node_4_settings.yml'))

responses = []
for node in nodes:
    responses.append(node.call_method(method='get_storagepool_nodepool', storagepool_nodepool_id='v200_100gb_6gb'))

for response in responses:
    for node in response.nodepools:
        measure = "node_pool"
        tags = f"name={node.name},tier={node.tier}"
        fields = f"percent_used={node.usage.pct_used}"
        print(f"{measure},{tags} {fields}")
