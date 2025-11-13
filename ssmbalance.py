import requests
import os
from datetime import datetime

def make_api_call():
    url = "https://smmpanel.co/api/v2"
    
    # Get API key from environment variable
    api_key = os.environ.get('API_KEY')
    
    if not api_key:
        print("ERROR: API_KEY not found in environment variables")
        return
    
    # Your API parameters (adjust based on your needs)
    payload = {
        'key': api_key,
        'action': 'balance',  # Change this to your actual action
    }
    
    try:
        response = requests.post(url, data=payload)
        print(f"[{datetime.now()}] Status: {response.status_code}")
        print(f"Response: {response.text}")  # Changed to .text to see raw response
        
        # Try to parse JSON
        try:
            data = response.json()
            print(f"JSON Response: {data}")
        except:
            print("Response is not JSON format")
        
    except Exception as e:
        print(f"✗ Error occurred: {type(e).__name__}: {e}")

if __name__ == "__main__":
    make_api_call()
