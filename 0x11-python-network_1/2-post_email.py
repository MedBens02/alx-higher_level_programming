#!/usr/bin/python3
""""sends a POST request to the passed URL with the email as a param"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as resp:
        print(resp.read().decode("utf-8"))
