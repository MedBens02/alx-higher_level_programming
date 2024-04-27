#!/usr/bin/python3
"""sends a request and displays the value of the variable X-Request-Id"""
import sys
import requests

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers.get("X-Request-Id"))
