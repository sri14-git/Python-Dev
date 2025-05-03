import requests as rq
api_key="ebbc07135b2247dfbf847efbcdf29df0"
url="https://newsapi.org/v2/everything?q=tesla&from=2025-04-03" \
    "&sortBy=publishedAt&apiKey=ebbc07135b2247dfbf847efbcdf29df0&language=en"
request=rq.get(url)
content=request.json()
for item in content["articles"]:
    print(item["title"])
    print(item["description"])
