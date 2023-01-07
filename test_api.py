import requests

url = "https://api.openweathermap.org/geo/1.0/direct?q=Barcelona&appid=7352aab4191e80ae6931d605ea6c9a43"
response = requests.get(url).json()
city = response[0]
print(f"{city['name']}: ({city['lat']}, {city['lon']})")
