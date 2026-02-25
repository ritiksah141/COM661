# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
# This keeps our API key secure and not hardcoded in the code
load_dotenv()

# Create a Flask application instance
# __name__ tells Flask where to look for templates and static files
app = Flask(__name__)

# Get the API key from environment variables
# We store sensitive data like API keys in .env file
RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')
RAPIDAPI_HOST = "open-weather13.p.rapidapi.com"


# Route decorator - tells Flask what URL should trigger this function
@app.route('/')
def index():
    """
    This is the home page route
    When someone visits the root URL (/), this function runs
    It returns the HTML template for our weather app
    """
    return render_template('index.html')


@app.route('/weather', methods=['POST'])
def get_weather():
    """
    This route handles weather data requests
    It receives a city name from the frontend
    Makes an API call to RapidAPI OpenWeather
    Returns the weather data as JSON
    """
    try:
        # Get the city name from the form data sent by the frontend
        # request.json gets the JSON data sent in the POST request
        data = request.json
        city = data.get('city', '')
        
        if not city:
            return jsonify({'error': 'Please enter a city name'}), 400
        
        # RapidAPI OpenWeather endpoint
        url = f"https://{RAPIDAPI_HOST}/city/{city}"
        
        # Headers required by RapidAPI
        # These authenticate our request
        headers = {
            'X-RapidAPI-Key': RAPIDAPI_KEY,
            'X-RapidAPI-Host': RAPIDAPI_HOST
        }
        
        # Make the API request
        # requests.get() sends a GET request to the API
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            weather_data = response.json()
            
            # Extract and organize the data we need
            # This makes it easier to use in our frontend
            result = {
                'city': weather_data.get('name', city),
                'country': weather_data.get('sys', {}).get('country', ''),
                'temperature': round(weather_data.get('main', {}).get('temp', 0)),
                'feels_like': round(weather_data.get('main', {}).get('feels_like', 0)),
                'description': weather_data.get('weather', [{}])[0].get('description', ''),
                'icon': weather_data.get('weather', [{}])[0].get('icon', '01d'),
                'humidity': weather_data.get('main', {}).get('humidity', 0),
                'wind_speed': round(weather_data.get('wind', {}).get('speed', 0)),
                'pressure': weather_data.get('main', {}).get('pressure', 0),
            }
            
            return jsonify(result)
        else:
            # If the API request failed, return an error
            return jsonify({'error': 'City not found. Please try again.'}), 404
            
    except Exception as e:
        # Catch any unexpected errors
        # In production, you'd want to log this error
        return jsonify({'error': 'An error occurred. Please try again later.'}), 500


# This runs the Flask development server
# debug=True automatically reloads the server when you make changes
# Only use debug=True in development, not in production!
if __name__ == '__main__':
    app.run(debug=True)