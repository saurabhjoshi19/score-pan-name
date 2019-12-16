import requests

url = "http://localhost:8000/getScore"

payload = "{\n\t\"applicant_name\" : \"saurabh joshi\",\n\t\"pan_name\" : \"soraubh joshi\"\n}"

headers = {
    'content-type': "application/json",
    'User-Agent': "PostmanRuntime/7.20.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "82152a25-a343-4599-9330-9ad12ef19c26,9cef2681-aad6-4ad4-9c88-263615379529",
    'Host': "localhost:8000",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "70",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

for i in range(10000):
    response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
