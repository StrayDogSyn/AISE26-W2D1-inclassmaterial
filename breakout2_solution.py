"""
JTC Program: AISE 25
W2D1 Breakout #2: Interacting with the OpenWeather API via a command line app

This script provides a command-line interface for querying weather data from the OpenWeather API.
It includes robust error handling, API key management, and optional extended features.

Author: Solution
Date: Oct 6, 2025
"""

import requests
import json
from datetime import datetime
from typing import Optional, Dict, List
import sys


class WeatherApp:
    """
    A command-line weather application that interfaces with the OpenWeather API.
    
    Attributes:
        api_key: OpenWeather API key
        base_url: Base URL for OpenWeather API
        current_location: Currently set location
        weather_data: Cached weather data for current location
        log_messages: List of messages to be logged
    """
    
    def __init__(self, api_key: str):
        """
        Initialize the WeatherApp with an API key.
        
        Args:
            api_key: Valid OpenWeather API key
        """
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.current_location = None
        self.weather_data = None
        self.log_messages: List[str] = []
        
    def log(self, message: str) -> None:
        """
        Add a message to the log.
        
        Args:
            message: Message to log
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.log_messages.append(log_entry)
        
    def fetch_weather(self, city: str) -> Optional[Dict]:
        """
        Fetch weather data from OpenWeather API for a given city.
        
        Args:
            city: Name of the city to query
            
        Returns:
            Dictionary containing weather data, or None if request fails
        """
        try:
            # Construct API request parameters
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'imperial'  # Use Fahrenheit for temperature
            }
            
            # Make API request
            self.log(f"Fetching weather data for: {city}")
            response = requests.get(self.base_url, params=params, timeout=10)
            
            # Check if request was successful
            if response.status_code == 200:
                data = response.json()
                self.log(f"Successfully retrieved weather data for {city}")
                return data
            elif response.status_code == 401:
                error_msg = "Error: Invalid API key. Please check your API key."
                print(error_msg)
                self.log(error_msg)
                return None
            elif response.status_code == 404:
                error_msg = f"Error: City '{city}' not found. Please check the spelling."
                print(error_msg)
                self.log(error_msg)
                return None
            else:
                error_msg = f"Error: API request failed with status code {response.status_code}"
                print(error_msg)
                self.log(error_msg)
                return None
                
        except requests.exceptions.Timeout:
            error_msg = "Error: Request timed out. Please check your internet connection."
            print(error_msg)
            self.log(error_msg)
            return None
        except requests.exceptions.ConnectionError:
            error_msg = "Error: Could not connect to OpenWeather API. Please check your internet connection."
            print(error_msg)
            self.log(error_msg)
            return None
        except Exception as e:
            error_msg = f"Error: An unexpected error occurred: {e}"
            print(error_msg)
            self.log(error_msg)
            return None
    
    def display_basic_weather(self, weather_data: Dict) -> None:
        """
        Display basic weather information (temperature and condition).
        
        Args:
            weather_data: Dictionary containing weather data from API
        """
        try:
            # Extract relevant information
            city = weather_data['name']
            country = weather_data['sys']['country']
            temp = weather_data['main']['temp']
            weather_main = weather_data['weather'][0]['main']
            weather_desc = weather_data['weather'][0]['description']
            
            # Display formatted weather information
            output = f"\n{'=' * 60}\n"
            output += f"Weather in {city}, {country}\n"
            output += f"{'=' * 60}\n"
            output += f"Temperature: {temp}°F\n"
            output += f"Condition: {weather_main} ({weather_desc})\n"
            output += f"{'=' * 60}\n"
            
            print(output)
            self.log(f"Displayed weather for {city}: {temp}°F, {weather_main}")
            
        except KeyError as e:
            error_msg = f"Error: Missing expected data in API response: {e}"
            print(error_msg)
            self.log(error_msg)
    
    def set_location(self, city: str) -> bool:
        """
        Set the current location and fetch weather data.
        
        Args:
            city: Name of the city to set as current location
            
        Returns:
            True if successful, False otherwise
        """
        weather_data = self.fetch_weather(city)
        
        if weather_data:
            self.current_location = city
            self.weather_data = weather_data
            
            # Display time, temperature, and weather description
            try:
                temp = weather_data['main']['temp']
                weather_main = weather_data['weather'][0]['main']
                current_time = datetime.now().strftime("%I:%M %p")
                
                output = f"\n✓ Location set to: {weather_data['name']}, {weather_data['sys']['country']}\n"
                output += f"Time: {current_time}\n"
                output += f"Temperature: {temp}°F\n"
                output += f"Weather: {weather_main}\n"
                
                print(output)
                self.log(f"Location set to: {city}")
                return True
                
            except KeyError as e:
                error_msg = f"Error: Missing expected data: {e}"
                print(error_msg)
                self.log(error_msg)
                return False
        
        return False
    
    def get_weather_detail(self, detail: str) -> None:
        """
        Display specific weather detail from cached data.
        
        Args:
            detail: Type of weather detail to display (e.g., 'temperature', 'pressure')
        """
        if not self.weather_data:
            print("Error: No location set. Use 'location <city>' to set a location first.")
            return
        
        detail = detail.lower().strip()
        
        try:
            # Map user-friendly terms to API data
            if detail in ['time', 'current time']:
                current_time = datetime.now().strftime("%I:%M %p on %B %d, %Y")
                print(f"Current time: {current_time}")
                
            elif detail in ['temperature', 'temp']:
                temp = self.weather_data['main']['temp']
                print(f"Temperature: {temp}°F")
                
            elif detail in ['feelslike', 'feels like', 'feels_like']:
                feels_like = self.weather_data['main']['feels_like']
                print(f"Feels like: {feels_like}°F")
                
            elif detail in ['pressure']:
                pressure = self.weather_data['main']['pressure']
                print(f"Pressure: {pressure} hPa")
                
            elif detail in ['sealevel', 'sea level', 'sea_level']:
                sea_level = self.weather_data['main'].get('sea_level', 'N/A')
                print(f"Sea level pressure: {sea_level} hPa" if sea_level != 'N/A' else "Sea level data not available")
                
            elif detail in ['windspeed', 'wind speed', 'wind_speed']:
                wind_speed = self.weather_data['wind']['speed']
                print(f"Wind speed: {wind_speed} mph")
                
            elif detail in ['winddirection', 'wind direction', 'wind_direction']:
                wind_deg = self.weather_data['wind']['deg']
                # Convert degrees to cardinal direction
                directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                            'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
                index = round(wind_deg / 22.5) % 16
                direction = directions[index]
                print(f"Wind direction: {direction} ({wind_deg}°)")
                
            elif detail in ['windgust', 'wind gust', 'wind_gust', 'gust']:
                wind_gust = self.weather_data['wind'].get('gust', 'N/A')
                print(f"Wind gust: {wind_gust} mph" if wind_gust != 'N/A' else "Wind gust data not available")
                
            elif detail in ['humidity']:
                humidity = self.weather_data['main']['humidity']
                print(f"Humidity: {humidity}%")
                
            elif detail in ['visibility']:
                visibility = self.weather_data.get('visibility', 'N/A')
                if visibility != 'N/A':
                    visibility_miles = visibility * 0.000621371  # Convert meters to miles
                    print(f"Visibility: {visibility_miles:.2f} miles")
                else:
                    print("Visibility data not available")
                    
            else:
                print(f"Unknown detail: '{detail}'")
                print("Available details: time, temperature, feelslike, pressure, sealevel, windspeed, winddirection, windgust, humidity, visibility")
            
            self.log(f"Retrieved detail: {detail}")
            
        except KeyError as e:
            print(f"Error: Data not available for '{detail}'")
            self.log(f"Error retrieving detail {detail}: {e}")
    
    def save_log(self, filename: str = "log.txt") -> None:
        """
        Save the log messages to a text file.
        
        Args:
            filename: Name of the log file
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("Weather App Session Log\n")
                f.write("=" * 60 + "\n\n")
                for message in self.log_messages:
                    f.write(message + "\n")
            
            print(f"✓ Log saved to {filename}")
            self.log(f"Log saved to {filename}")
            
        except Exception as e:
            error_msg = f"Error saving log: {e}"
            print(error_msg)
            self.log(error_msg)
    
    def print_help(self) -> None:
        """Display help information about available commands."""
        help_text = """
╔════════════════════════════════════════════════════════════════════╗
║                     WEATHER APP - HELP MENU                        ║
╚════════════════════════════════════════════════════════════════════╝

BASIC COMMANDS:
---------------
  <city name>       Query weather for a city (simple mode)
  q or quit         Exit the program

EXTENDED COMMANDS (Bonus):
--------------------------
  location <city>   Set the current location and display basic weather
  
  get <detail>      Get specific weather information for current location
                    Available details:
                    • time          - Current time
                    • temperature   - Current temperature
                    • feelslike     - "Feels like" temperature
                    • pressure      - Atmospheric pressure
                    • sealevel      - Sea level pressure
                    • windspeed     - Wind speed
                    • winddirection - Wind direction
                    • windgust      - Wind gust speed
                    • humidity      - Humidity percentage
                    • visibility    - Visibility distance
  
  log               Save session log to log.txt
  help              Display this help menu
  quit              Exit the program

EXAMPLES:
---------
  Simple mode:    New York
  Set location:   location London
  Get detail:     get temperature
  Get detail:     get windspeed

NOTES:
------
  • City names with spaces should be entered without quotes
  • Commands are case-insensitive
  • The API allows 60 calls per minute on the free tier
  • Use 'location' command to set location (queries API)
  • Use 'get' command to retrieve cached data (no API call)
"""
        print(help_text)
        self.log("Displayed help menu")
    
    def run_simple_mode(self) -> None:
        """Run the basic weather app (non-extended version)."""
        print("\n" + "=" * 60)
        print("Welcome to the Weather App!")
        print("=" * 60)
        print("Enter a city name to get weather information, or 'q' to quit.\n")
        
        self.log("Started Weather App (Simple Mode)")
        
        while True:
            # Prompt user for city name
            city = input("Please input a city (or q to quit): ").strip()
            
            # Check if user wants to quit
            if city.lower() == 'q':
                print("\nThank you for using the Weather App. Goodbye!")
                self.log("User quit the application")
                break
            
            # Skip empty input
            if not city:
                print("Please enter a valid city name.")
                continue
            
            # Fetch and display weather
            weather_data = self.fetch_weather(city)
            
            if weather_data:
                self.display_basic_weather(weather_data)
                print("\nThank you for using the Weather App. Goodbye!")
                self.log("User successfully retrieved weather and exited")
                break
    
    def run_extended_mode(self) -> None:
        """Run the extended weather app with additional commands."""
        print("\n" + "=" * 60)
        print("Welcome to the Weather App (Extended Mode)!")
        print("=" * 60)
        print("Type 'help' for a list of commands.\n")
        
        self.log("Started Weather App (Extended Mode)")
        
        while True:
            # Prompt user for command
            user_input = input(">>> ").strip()
            
            # Skip empty input
            if not user_input:
                continue
            
            # Parse command and arguments
            parts = user_input.split(maxsplit=1)
            command = parts[0].lower()
            args = parts[1] if len(parts) > 1 else ""
            
            # Process commands
            if command in ['quit', 'q', 'exit']:
                print("\nThank you for using the Weather App. Goodbye!")
                self.log("User quit the application")
                break
                
            elif command == 'help':
                self.print_help()
                
            elif command == 'location':
                if not args:
                    print("Error: Please provide a city name. Usage: location <city>")
                else:
                    self.set_location(args)
                    
            elif command == 'get':
                if not args:
                    print("Error: Please specify what detail to get. Usage: get <detail>")
                    print("Type 'help' to see available details.")
                else:
                    self.get_weather_detail(args)
                    
            elif command == 'log':
                self.save_log()
                
            else:
                # Treat as city name for backward compatibility
                print(f"\nQuerying weather for: {user_input}")
                weather_data = self.fetch_weather(user_input)
                if weather_data:
                    self.display_basic_weather(weather_data)


def load_api_key(filename: str = "api_key.txt") -> Optional[str]:
    """
    Load API key from a text file.
    
    Args:
        filename: Name of the file containing the API key
        
    Returns:
        API key as string, or None if file not found
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            api_key = f.read().strip()
            
        if not api_key:
            print(f"Error: {filename} is empty")
            return None
            
        return api_key
        
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        print(f"Please create a file named '{filename}' with your OpenWeather API key.")
        print("\nTo get an API key:")
        print("1. Create a free account at https://home.openweathermap.org")
        print("2. Find your key on openweathermap.org")
        print(f"3. Save it to a file named '{filename}' in this directory")
        return None
    except Exception as e:
        print(f"Error reading API key: {e}")
        return None


def main():
    """Main function to run the weather application."""
    # Load API key from file
    api_key = load_api_key()
    
    if not api_key:
        print("\nCannot proceed without an API key. Exiting.")
        return
    
    # Create weather app instance
    app = WeatherApp(api_key)
    
    # Ask user which mode to run
    print("\nSelect mode:")
    print("1. Simple mode (basic weather query)")
    print("2. Extended mode (with additional commands)")
    
    while True:
        choice = input("\nEnter choice (1 or 2): ").strip()
        
        if choice == '1':
            app.run_simple_mode()
            break
        elif choice == '2':
            app.run_extended_mode()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
