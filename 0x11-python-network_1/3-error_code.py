#!/usr/bin/python3
""""displays the value of the X-Request-Id"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('UTF-8'))
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
