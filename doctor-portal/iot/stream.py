import http.client

conn = http.client.HTTPSConnection("sandbox-api.dexcom.com")
code = conn.request(method="GET", url='https://api.dexcom.com/v2/oauth2/login?client_id={AfXS1cLqQmj3yCDqpm1v8Xt57nJtmdff}&redirect_uri={http://localhost:8888/}&response_type=code&scope=offline_access')
payload = "client_secret={fsGOSzcfZ72yVuyO}&client_id={AfXS1cLqQmj3yCDqpm1v8Xt57nJtmdff}&code={"+"code"+"}&grant_type=authorization_code&redirect_uri=(http://localhost:8888/}"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

conn.request("POST", "/v2/oauth2/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

#########################

headers = {
    'authorization': "Bearer {your_access_token}"
    }

conn.request("GET", "/v2/users/self/egvs?startDate=2017-06-16T15:30:00&endDate=2017-06-16T15:45:00", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))