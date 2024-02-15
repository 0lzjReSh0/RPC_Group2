# import json

from xmlrpc.server import SimpleXMLRPCServer

def get_weather(city):
    weather_data = {
        "lahti": {"temperature": "-12°C", "weather": "Sunny"},
        "helsinki": {"temperature": "-5°C", "weather": "Rainy"},
        "turku": {"temperature": "-14°C", "weather": "Cloudy"}
    }
    city = city.lower()
    return weather_data.get(city, "Can not find the City!")

server = SimpleXMLRPCServer(("localhost", 3000))
print("Listening on port 3000:")

server.register_function(get_weather, "getWeather")

server.serve_forever()
