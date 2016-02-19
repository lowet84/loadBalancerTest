import urllib.request
import sys
from collections import Counter

requests = int(sys.argv[1])

requestResponses = []
for x in range(0, requests):
    with urllib.request.urlopen('http://localhost/') as response:
        html = response.read().decode("utf-8")
        requestResponses.append(html)

requestResponses.sort()
values = Counter(requestResponses)
keys = list(values.keys())
keys.sort()

for x in keys:
    print("Node " + x + ": " + str(values.get(x)))

