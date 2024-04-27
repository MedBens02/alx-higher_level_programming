#!/usr/bin/python3
""""sends a request to the URL and displays the body of the response"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('UTF-8'))
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
