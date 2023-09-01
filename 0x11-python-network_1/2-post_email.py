#!/usr/bin/python3
"""Takes URL and email, sends POST request and displays body of response"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with email parameter
    data = urllib.parse.urlencode({'email': email}).encode('ascii')

    try:
        with urllib.request.urlopen(url, data=data) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.URLError as e:
        print(f"Error sending POST request: {e}")
