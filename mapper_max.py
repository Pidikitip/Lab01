#!/usr/bin/env python3

import sys

def mapper():
	for line in sys.stdin:
		try:
    			data = line.strip().split(",")
    			timestamp, city, item, cost = data
    			print(city + "," + cost)
		except ValueError:
    			continue

if __name__ == "__main__":
    # what function should run when python mapper.py is called?
	mapper()
