

import http.client

conn = http.client.HTTPSConnection("api.commerce.naver.com")

headers = { 'Authorization': "Bearer REPLACE_BEARER_TOKEN" }

conn.request("GET", "/external/v2/products/channel-products/%7BchannelProductNo%7D", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))