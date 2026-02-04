from flask import Flask, render_template, request
import requests
import os  # NEW: Imports the operating system tools
from dotenv import load_dotenv  # NEW: Imports the tool to read .env files

# NEW: This command finds the .env file and loads the variables
load_dotenv()

app = Flask(__name__)

# CONFIGURATION
# ---------------------------------------------------------
# We are using the "JSearch" API endpoint as a standard example.
# If your API is different (e.g. "Active Jobs DB"), 
# you just need to update the API_URL.
API_URL = "https://jsearch.p.rapidapi.com/search"

# NEW: We get the key from the environment instead of hardcoding it
API_KEY = os.getenv("RAPIDAPI_KEY")

HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}
# ---------------------------------------------------------

@app.route('/', methods=['GET', 'POST'])
def home():
    jobs = []
    error = None
    
    # Variables to keep the form filled after searching
    current_role = ""
    current_loc = ""
    current_type = ""

    if request.method == 'POST':
        # 1. Get all the form data
        current_role = request.form.get('job_role')
        current_loc = request.form.get('location')
        current_type = request.form.get('job_type') # e.g., 'INTERN', 'FULLTIME'
        
        # 2. Build the smart query string
        # If user types "Python" and Location "London", query becomes "Python in London"
        final_query = current_role
        if current_loc:
            final_query = f"{current_role} in {current_loc}"

        # 3. Set up the API parameters
        querystring = {
            "query": final_query,
            "page": "1",
            "num_pages": "1"
        }

        # 4. Add Job Type filter ONLY if the user selected one
        if current_type:
            querystring["employment_types"] = current_type

        try:
            response = requests.get(API_URL, headers=HEADERS, params=querystring)
            data = response.json()

            if response.status_code == 200 and 'data' in data:
                jobs = data['data']
            else:
                error = "No jobs found."
                
        except Exception as e:
            error = f"Connection error: {e}"

    # Pass the 'current_*' variables back so the form stays filled
    return render_template('index.html', 
                           jobs=jobs, 
                           error=error,
                           current_role=current_role,
                           current_loc=current_loc,
                           current_type=current_type)

# ---------------------------------------------------------
# NEW ROUTE: Job Details Page
# This function runs when you go to /job/12345
# ---------------------------------------------------------
@app.route('/job/<job_id>')
def job_details(job_id):
    # We use a different endpoint: /job-details
    details_url = "https://jsearch.p.rapidapi.com/job-details"
    
    querystring = {
        "job_id": job_id,
        "extended_publisher_details": "false"
    }

    try:
        response = requests.get(details_url, headers=HEADERS, params=querystring)
        data = response.json()
        
        # The API returns a list called 'data'. We want the first item.
        if response.status_code == 200 and 'data' in data and len(data['data']) > 0:
            job = data['data'][0]
            return render_template('job_details.html', job=job)
        else:
            return "<h3>Job not found or API Error</h3><a href='/'>Go Home</a>"
            
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    # Running on localhost port 5000
    app.run(debug=True)