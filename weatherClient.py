from xmlrpc.client import ServerProxy

server = ServerProxy("http://localhost:3000/")

while True:
    city = input("Input the city name (type 'end' to stop): ")
    if city == 'end':
        print("Client side end.")
        break

    try:
        weather_info = server.getWeather(city)
        print(f"Weather for {city} is: {weather_info}")
    except Exception as e:
        print(f"Error: {e}")
