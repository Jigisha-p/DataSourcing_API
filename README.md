## Introduction
A common way of collecting data is through APIs. Those can be <a href="https://github.com/public-apis/public-apis">public APIs</a> with authentication or not, free or paid, internal APIs at your company, etc.

When it comes to APIs, there are some keywords that you should understand:

- <a href="https://en.wikipedia.org/wiki/SOAP">SOAP </a>(old)
- <a href="https://en.wikipedia.org/wiki/Representational_state_transfer">REST </a> (current)
- <a href="https://en.wikipedia.org/wiki/GraphQL">GraphQL </a>(very new, less frequent)
- <a href="https://en.wikipedia.org/wiki/XML">XML </a>(long-established)
- <a href="https://en.wikipedia.org/wiki/JSON">JSON </a>(currently very widespread)

The first three keywords refer to an architecture or a protocol on top of HTTP(s) and it is really important to figure out which one you are using when you want to consume data from an API.

The last two keywords refer to a <b>data format </b> that would usually be sent back to you when performing an API call.

ℹ️ Most modern APIs are RESTful and send back JSON. In this project, such an API is used.

## Reading the documentation
When presented with a new API to use, your first reflex should be to go straight to the documentation, and figure out the following:

1. Is this a REST API?
2. Does it serve JSON?
3. Does this API require authentication? (do I need to sign up to get an API key? Do I need to pay?)
4. What is the base URI?
5. Which endpoints can I call? What data does it return?

Go to <a href="https://openweathermap.org/api">OpenWeatherMap</a> API documentation read it, and try answering those questions.

## Authentication 
You might have noticed that OpenWeatherMap requires you to sign up for an API key. Even though OpenWeatherMap offers a <a href="https://openweathermap.org/price">number of free API calls</a>, they still want to know how different users consume the API (and track if you hit your API call limit 😜). This is the norm for most APIs out there.

Sign up for an API key (which might take 10-20 minutes to get activated)

## Making a test call to the API
Before building something fancy, we need to first make sure that we can run an API call successfully. This is a sanity check to make sure we don’t start coding too much before realizing that the API we intended to use is not a good fit.

So how can we make our first call? There are several options:

### Using the browser
The browser is an HTTP client! If there is no complex request Header to set and the verb to use is GET, then it’s just as easy as typing the URL in the address bar. 

Open a new browser tab, and copy/paste the following URL:
```bash
https://api.openweathermap.org/geo/1.0/direct?q=Barcelona&appid=XXXXXXXXXXX
```
What do you see? If you are on Chrome, you should install the JSONView extension for a neater look. In the end, JSON is just text that needs to be parsed, that’s what the extension will do.

### Optional - Using Postman
<a href="https://www.postman.com/">Postman </a> is an app that many developers download on their laptop to use when building software consuming APIs. It provides a more advanced experience where you need to have more control over:

- HTTP verb (GET, POST, PATCH, DELETE, etc.)
- Request headers (Content-Type, Authorization, etc.)
- Request body (application/x-www-form-urlencoded or raw)
This application allows us to save some requests, create tabs with different requests and offers more advanced features. 

### Using Python
Finally, we want to use this API in our code. Python’s standard library comes with an <a href="https://docs.python.org/3/library/http.client.html" >http.client</a> built-in module, but we are not going to use it. Instead, we are going to use the <a href="https://requests.readthedocs.io/en/latest/">requests</a> library, an ‘elegant and simple HTTP library for Python, built for human beings’.

Open the test_api.py file and paste the following code:
```bash
import requests

url = "https://api.openweathermap.org/geo/1.0/direct?q=Barcelona&appid=XXXXXXXXXXX"
response = requests.get(url).json()
city = response[0]
print(f"{city['name']}: ({city['lat']}, {city['lon']})")
```
Save the file and run the following command:
```bash
python test_api.py
```

# The Project:
This is a weather CLI using the API. Here’s the flow:

1. Launch the app with python weather.py
2. Get asked to type a city name
3. If city is unknown to the API, display an error message and go back to step 2.
4. Fetch the weather forecast for the next 5 days and display it (Date, Weather and max temperature in °C)
5. Go back to step 2 (loop to ask for a new city).
6. At any point, Ctrl-C can be used to quit the program

In action, it should look like this:
```bash
python weather.py
```
```
City?
> london
1. London,GB
2. City of London,GB
3. London,CA
4. Chelsea,GB
5. London,US
Multiple matches found, which city did you mean?
> 1
2023-01-07: Clouds (12°C)
2023-01-08: Clouds (8°C)
2023-01-09: Clouds (7°C)
2023-01-10: Clouds (6°C)
2023-01-11: Clouds (9°C)
City?
```
>


### Minimum setup:
```bash
pip install --upgrade pip
pip install -r requirements.txt
pip list
```
