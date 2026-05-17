import requests
import sys

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "YOUR_API_KEY"   


def main():
    CITY = input("Enter the name of city :- ")

    
    request_url = f"{BASE_URL}?q={CITY}&appid={API_KEY}"

    try:
        
        response = requests.get(request_url)
        response.raise_for_status()

        data = response.json()

        
        city_name = data["name"]
        temperature = data["main"]["temp"] - 273.15
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        
        print()
        print(f"Weather in {city_name}:")
        print("-" * 25)
        print(f"Temperature: {round(temperature, 2)} °C")
        print(f"Humidity: {humidity} %")
        print(f"Conditions: {description.capitalize()}")

    except requests.exceptions.HTTPError as http_err:
        print()

        if http_err.response.status_code == 401:
            print("Error: Invalid API Key.")
        elif http_err.response.status_code == 404:
            print("Error: City not found. Please check spelling.")
        else:
            print(f"An HTTP error occurred: {http_err}")

        sys.exit(1)

    except requests.exceptions.RequestException as e:
        print()
        print("Network error: Could not connect to weather service.")
        print(f"Details: {e}")
        sys.exit(1)



if __name__ == "__main__":
    main()