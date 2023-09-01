#!/usr/bin/python3
"""POST an email"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the email parameter
    data = {'email': email}
    # Send the POST request to the URL with email parameter
    response = requests.post(url, data=data)
    # Display body of response
    print(response.text)
