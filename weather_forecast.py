import requests
import json
import sys

def get_weather(city):
    # Set the OpenWeatherMap API key here
    api_key = 'b93d03648b3b07112a0a416cab284a57'

    # Construct the API URL
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        # Make a GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-2xx status codes

        # Parse the JSON response
        data = response.json()

        # Extract relevant weather information
        weather = data['weather'][0]['main']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Print the weather forecast
        print(f'Weather forecast for {city}:')
        print(f'Conditions: {weather}')
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Wind Speed: {wind_speed} m/s')

    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        sys.exit(1)

    except (KeyError, IndexError):
        print(f'Failed to retrieve weather data for {city}. Please try again.')
        sys.exit(1)

if __name__ == '__main__':
    # Check if a city name is provided as a command-line argument
    if len(sys.argv) < 2:
        print('Please provide a city name as an argument.')
        sys.exit(1)

    city_name = ' '.join(sys.argv[1:])

    # Fetch and display the weather forecast
    get_weather(city_name)
