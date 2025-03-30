import requests

API_KEY = "212ad9ecd3d14f047e120782d93ee627"

# Weather condition mapping to ASCII symbols
WEATHER_ICONS = {
    "clear": "☀️ Sunny",
    "clouds": "☁️ Cloudy",
    "rain": "🌧️ Rainy",
    "thunderstorm": "⛈️ Thunderstorm",
    "drizzle": "🌦️ Light Rain",
    "snow": "❄️ Snowy",
    "mist": "🌫️ Misty",
    "fog": "🌁 Foggy",
}

def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={API_KEY}&units=metric"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]
        condition = weather['main'].lower()

        # Select appropriate weather symbol
        weather_icon = WEATHER_ICONS.get(condition, "❓ Unknown Weather")

        print("\n=========================")
        print(f"   🌍 Weather Report: {city_name}")
        print("=========================")
        print(f"   {weather_icon}")
        print("   ----------------------")
        print(f"   🌡️  Temperature: {main['temp']}°C".upper())
        print(f"   💧 Humidity: {main['humidity']}%")
        print(f"   💨 Wind Speed: {wind['speed']} m/s")
        print("=========================\n")

    else:
        print(f"City {city_name} not found.")

while True:
    city = input("Enter the city name (or 'exit' to quit): ")
    if city.lower() == 'exit':
        break
    get_weather(city)
