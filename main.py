import  requests
from datetime import datetime
My_Lat= 40.958149
My_Long=-73.003761
formatted = 0

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# print(response.status_code)
#
# data = response.json()
# print(data)
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position= (longitude,latitude)
# print(iss_position)
parameters ={
    "lat": My_Lat,
    "lng" : My_Long,
    "formatted":formatted

}

response1 = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
response1.raise_for_status()
print(response1)
data = response1.json()
print(data)
sunrise = data["results"]["sunrise"]
print(sunrise)
time_now= datetime.now()
print(time_now)