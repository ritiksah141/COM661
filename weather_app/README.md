# 🌤️ SkyWatch - Weather App

A beautiful weather application built with Flask and RapidAPI's OpenWeather API. Perfect for beginners learning web development!

## 📸 Features

- 🔍 Search weather by city name
- 🌡️ Display temperature, humidity, wind speed, and pressure
- 🎨 Beautiful, animated gradient background
- 📱 Responsive design (works on mobile and desktop)
- ⚡ Fast and lightweight

## 🛠️ Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **API**: RapidAPI OpenWeather API
- **Environment**: python-dotenv for secure API key management

## 📋 Prerequisites

Before you start, make sure you have:

1. **Python 3.8 or higher** installed on your computer
   - Check by running: `python --version` or `python3 --version`
   - Download from: https://www.python.org/downloads/

2. **A RapidAPI account** (free)
   - Sign up at: https://rapidapi.com/

## 🚀 Installation & Setup

### Step 1: Get Your API Key

1. Go to https://rapidapi.com/worldapi/api/open-weather13
2. Click "Sign Up" (if you don't have an account)
3. Click "Subscribe to Test" and select the **FREE plan**
4. Copy your API key from the "X-RapidAPI-Key" in the code snippets

### Step 2: Set Up the Project

1. **Download/Clone this project** to your computer

2. **Open Terminal/Command Prompt** in the project folder

3. **Create a virtual environment** (recommended):
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```
   
   What is a virtual environment? It's like a separate Python workspace for this project, so packages don't conflict with other projects.

4. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```
   
   This reads the `requirements.txt` file and installs all the packages we need.

5. **Configure your API key**:
   - Open the `.env` file
   - Replace `your_rapidapi_key_here` with your actual RapidAPI key
   - Save the file
   
   Example:
   ```
   RAPIDAPI_KEY=abc123xyz456yourkey
   ```
   
   ⚠️ **IMPORTANT**: Never share your `.env` file or commit it to Git!

### Step 3: Run the Application

1. Make sure your virtual environment is activated (you should see `(venv)` in your terminal)

2. Run the Flask app:
   ```bash
   python app.py
   ```
   
   or on some systems:
   ```bash
   python3 app.py
   ```

3. You should see output like:
   ```
   * Running on http://127.0.0.1:5000
   * Debug mode: on
   ```

4. **Open your browser** and go to: `http://127.0.0.1:5000` or `http://localhost:5000`

5. 🎉 Your weather app is now running!

## 📂 Project Structure

```
weather-app/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API key)
├── .gitignore            # Files to ignore in Git
├── README.md             # This file
│
└── templates/
    └── index.html        # Frontend HTML template
```

## 🎓 Understanding the Code

### app.py (Backend)

- **Flask**: A web framework that handles HTTP requests and serves HTML
- **Routes**: URLs that trigger specific functions (e.g., `/` for homepage, `/weather` for API calls)
- **API Request**: Uses the `requests` library to fetch data from RapidAPI
- **JSON**: A data format for sending/receiving information between frontend and backend

### index.html (Frontend)

- **HTML**: Structure of the webpage
- **CSS**: Styling and animations (the beautiful gradient background!)
- **JavaScript**: Handles user interactions and makes API calls to our Flask backend
- **Fetch API**: Modern way to make HTTP requests from JavaScript

### .env File

- Stores sensitive information like API keys
- Keeps secrets out of your code
- Never commit this file to version control (that's why it's in `.gitignore`)

## 🔧 How It Works

1. User enters a city name and clicks "Search"
2. JavaScript captures the form submission
3. JavaScript sends a POST request to `/weather` endpoint with the city name
4. Flask receives the request and extracts the city name
5. Flask makes an API call to RapidAPI OpenWeather
6. RapidAPI returns weather data
7. Flask processes and sends the data back to JavaScript
8. JavaScript updates the webpage with the weather information

## 🎨 Customization Ideas

Want to make it your own? Try these:

1. **Change Colors**: Modify the CSS variables in `index.html`:
   ```css
   :root {
       --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
   }
   ```

2. **Add More Data**: The API returns lots of info! Try adding:
   - Sunrise/sunset times
   - Cloud coverage
   - Visibility

3. **Add a 5-Day Forecast**: Use a different endpoint to show future weather

4. **Save Favorite Cities**: Use browser localStorage to remember searched cities

## 🐛 Troubleshooting

### "Module not found" error
- Make sure your virtual environment is activated
- Run `pip install -r requirements.txt` again

### "City not found" error
- Check your spelling
- Try adding the country (e.g., "London, UK")

### "API key invalid" error
- Double-check your API key in the `.env` file
- Make sure there are no extra spaces
- Verify you're subscribed to the API on RapidAPI

### App won't start
- Check if port 5000 is already in use
- Try changing the port: `app.run(debug=True, port=5001)`

## 📚 Learning Resources

- **Flask Documentation**: https://flask.palletsprojects.com/
- **Python Requests Library**: https://requests.readthedocs.io/
- **MDN Web Docs (JavaScript)**: https://developer.mozilla.org/
- **CSS Tricks**: https://css-tricks.com/

## 🤝 Next Steps

Congratulations on building your weather app! Here's what you can learn next:

1. **Deploy your app**: Learn to host it online using Heroku, PythonAnywhere, or Render
2. **Add a database**: Store user searches using SQLite or PostgreSQL
3. **User authentication**: Let users create accounts and save preferences
4. **Build a REST API**: Create your own API endpoints
5. **Learn React**: Build more complex frontend applications

## 📝 License

This project is free to use for learning purposes!

## 🆘 Need Help?

If you get stuck:
1. Read the error message carefully
2. Check the code comments
3. Search for the error on Google/Stack Overflow
4. Review Flask and Python documentation

Happy coding! 🚀