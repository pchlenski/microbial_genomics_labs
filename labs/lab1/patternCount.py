#!/usr/bin/python
import argparse

def get_options():
	description = "Match patterns within strings"
	parser = argparse.ArgumentParser(description = description,prog = 'patternCount.py')
	parser.add_argument('text', action='store',help='DNA sequence string')
	parser.add_argument('pattern', action='store',help='Pattern for matching')
	return parser.parse_args()

def patternCount(text,pattern):
	count = 0
	num_text = len(text)
	num_pattern = len(pattern)
	for i in range(num_text-num_pattern):
		if text[i:i+num_pattern] == pattern:
			count = count+1
	return count

if __name__ == "__main__":
    options = get_options()
    num_matches = patternCount(options.text,options.pattern)
    print("Number matches = {}".format(num_matches))