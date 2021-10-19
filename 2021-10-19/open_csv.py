import urllib.request

with urllib.request.urlopen("https://www.google.com/") as response:
    html = response.read()
    print(html)
