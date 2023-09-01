#!/usr/bin/python3
"""Take in a letter and send a POST request with the letter as parameter"""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    # Get the letter from commandline arguments or empty string if not provided
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    # Send POST request with letter as parameter
    response = requests.post(url, data={'q': q})
    try:
        # Try to parse the JSON response
        data = response.json()
        # Check if JSON is not empty
        if data:
            # Display the id name from the JSON
            print(f"[{data['id']}] {data['name']}")
        else:
            # If the JSON is empty, display no result
            print("No result")
    except ValueError:
        print("Not a valid JSON")
