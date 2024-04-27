#!/usr/bin/python3
"""sends a POST request to
   http://0.0.0.0:5000/search_user
   with the letter as a param
"""
import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    req = requests.post("http://0.0.0.0:5000/search_user", {"q": letter})
    try:
        resp = req.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
