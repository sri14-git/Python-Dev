import requests as rq




API=""
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