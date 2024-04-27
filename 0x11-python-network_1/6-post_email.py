#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a param"""
import sys
import requests

if __name__ == "__main__":
    req = requests.post(sys.argv[1], {"email": sys.argv[2]})
    print(req.text)
