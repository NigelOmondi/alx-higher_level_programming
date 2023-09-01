#!/usr/bin/python3
"""Display the value of 'X-Request-Id' variable found in response header"""

import sys
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            headers = response.info()
            x_request_id = headers.get('X-Request-Id')
            if x_request_id:
                print(x_request_id)

    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e}")
