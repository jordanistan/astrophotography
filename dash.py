from flask import Flask, render_template
import requests

app = Flask(__name__)

# Assume that the API key is correctly set in environment variables or configuration
API_KEY = 'API-TOKEN'
APOD_URL = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}'

def get_deep_space_objects():
    try:
        # Make a request to NASA's skywatch API to fetch data
        response = requests.get(APOD_URL)
        response.raise_for_status()

        data = response.json()
        
        # Format the date with a year and extract only the needed fields
        date_parts = data['date'].split('-')
        formatted_date = f"{date_parts[1]} {date_parts[2]}, {date_parts[0]}"
        name = data.get('title', 'N/A')  # Provide a default value if key doesn't exist
        location = data.get('location', 'N/A')  # Provide a default value if key doesn't exist
        
        return [{'name': name, 'best_time_to_view': formatted_date, 'location': location}]
    except (requests.RequestException, ValueError) as e:
        # Log the error or handle it appropriately
        print(e)
        return []  # Return an empty list if the request failed or JSON was invalid

@app.route('/')
def dashboard():
    objects = get_deep_space_objects()
    return render_template('dashboard.html', objects=objects)

if __name__ == '__main__':
    app.run(debug=True)

