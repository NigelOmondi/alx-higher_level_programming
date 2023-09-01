#!/usr/bin/python3
"""Fetch https://alx-intranet.hbtn.io/status using requests library"""
import requests

url = 'https://alx-intranet.hbtn.io/status'

if __name__ == "__main__":
    response = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
