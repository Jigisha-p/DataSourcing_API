import requests

url = "https://api.openweathermap.org/geo/1.0/direct?q=Barcelona&appid=xxxxxxxxxxxx"
response = requests.get(url).json()
city = response[0]
print(f"{city['name']}: ({city['lat']}, {city['lon']})")
