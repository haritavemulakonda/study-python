import json
import urllib.request

request = urllib.request.Request("https://nominatim.openstreetmap.org/search.php?q=sydney&format=jsonv2")

with urllib.request.urlopen(request) as response:
    loaded_file = json.loads(response.read())
    print(json.dumps(loaded_file, indent=4))

print("-" * 200)
print("{:35}|{:40}|{:40}|{:100}".format('latitude', 'longitude', 'type', 'Display name'))
print("-" * 200)

for content in loaded_file:
    print(f"{content['lat']:35} | {content['lon']:40} |{content['type']:40} | {content['display_name']:100}")

print("-" * 200)
