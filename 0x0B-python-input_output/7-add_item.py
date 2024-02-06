#!/usr/bin/python3
'''Adds args to a list and saves it to a file'''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = list(sys.argv[1:])

try:
    objs = load_from_json_file("add_item.json")
except FileNotFoundError:
    objs = []
objs.extend(args)
save_to_json_file(objs, "add_item.json")
