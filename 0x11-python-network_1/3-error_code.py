#!/usr/bin/python3
"""Manage HTTPError exception and print error code"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
