import json
import requests

# def get_data():

url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-FDA1EAB2-E1DE-4F0C-8E41-7026A551403E&locationName=%E8%87%BA%E5%8D%97%E5%B8%82"
params = { "Authorization": "CWB-FDA1EAB2-E1DE-4F0C-8E41-7026A551403E",
    "locationName": "%E8%87%BA%E5%8D%97%E5%B8%82"

}

response = requests.get(url, params=params)
print(response.status_code)

if response.status_code == 200:
    print(response.text)
    data = json.loads(response.text)

    location = data["records"]["location"][0]["locationName"]
    weather_elements = data["records"]["location"][0]["weatherElement"]
    rain_prob = weather_elements[1]["time"][0]["parameter"]["parameterName"]
    min_tem = weather_elements[2]["time"][0]["parameter"]["parameterName"]
    max_tem = weather_elements[4]["time"][0]["parameter"]["parameterName"]

    print(location)
    print(rain_prob)
    print(min_tem)
    print(max_tem)

else:
    print("Can't get data!")

