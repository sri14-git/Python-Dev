import requests as rq




API="f1d1f33de2890face944c1b5436dcff2"
def getdata(place,forecast_days=None):
    url="https://api.openweathermap.org/data/2.5" \
        f"/forecast?q={place}" \
        f"&appid={API}"
    response=rq.get(url)
    data=response.json()
    nv=8*forecast_days
    fildata=data["list"][:nv]
    return fildata
if __name__=="__main__":
    print(getdata("chennai",2,"Sky"))