import urllib.request
url = 'http://www.bom.gov.au/climate/dwo/202110/text/IDCJDW2061.202110.csv'
req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)



