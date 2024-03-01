#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to
the URL and displays the body of the response"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError:
        print(f"Error code: {response.status_code}")