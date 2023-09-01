#!/usr/bin/python3
"""Print error codes"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)
    # Display the body of response
    print(response.text)
    # Check HTTP status code and print error message if > 400
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
