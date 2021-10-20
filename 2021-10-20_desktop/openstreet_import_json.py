import json
import urllib.request

request = urllib.request.Request("https://nominatim.openstreetmap.org/search.php?q=sydney&format=jsonv2")

with urllib.request.urlopen(request) as response:
    loaded_data = json.loads(response.read())
    # formatted_data = json.dumps(loaded_data, indent= 4)
    # print(formatted_data)

"""Printing Header for the below content"""
header = ["Display Name", "Latitude", "Longitude", "Type"]
print("{:135}{:20}{:20}{:100}".format('Display name', 'latitude', 'longitude', 'type', ))
print("-"*200)

"""Printing loaded_data while selecting specific fields"""
for content in loaded_data:
    print(f"{content['display_name'].ljust(135)}"
          f"{content['lat'].ljust(20)}"
          f"{content['lon'].ljust(20)}"
          f"{content['type']}")
