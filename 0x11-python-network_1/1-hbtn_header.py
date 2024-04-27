#!/usr/bin/python3
""""displays the value of the X-Request-Id"""
import sys
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
