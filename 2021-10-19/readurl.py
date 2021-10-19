#!/usr/bin/python3

import urllib.request

req = urllib.request.Request(
    url="http://www.bom.gov.au/climate/dwo/202110/text/IDCJDW2061.202110.csv",
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

urlreq = urllib.request.urlopen(req)
print(urlreq.read().decode)

i = 0
list = []
for l in urlreq.readlines():
    print(i, "\t", l)
i += 1
if i > 7:
    list.append(l.decode())
print(list)

