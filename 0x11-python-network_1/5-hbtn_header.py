#!/usr/bin/python3
"""Display the value of X-Request-Id in the response header"""
import requests
import sys

if __name__ == "__name__":
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')

    print(x_request_id)
