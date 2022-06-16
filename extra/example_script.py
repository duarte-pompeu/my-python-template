import http.client
import json

conn = http.client.HTTPSConnection("api.adviceslip.com")
conn.request("GET", "/advice")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()  # This will return entire content.
# The following example demonstrates reading data in chunks.
jstr = str(data1, "utf-8")
d = json.loads(jstr)
print(d["slip"]["advice"])
