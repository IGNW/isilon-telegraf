#! /usr/bin/env python3
from isilon import Isilon

# The Isilon class sets up the connection to the Isilon and provides an object
i = Isilon(api_class="StatisticsApi")

response = i.call_method(method='get_summary_drive')

for drive in response.drive:
    if drive.type != "UNKNOWN":
        measure = "drive"
        tags = f"drive_id={drive.drive_id},type={drive.type}"
        fields = f"percent_used={drive.used_bytes_percent}"
        print(f"{measure},{tags} {fields}")
