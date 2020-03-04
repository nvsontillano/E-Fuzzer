import urllib.parse
import sys

file = sys.argv[1]

with open(file, 'r') as rf:
	contents = rf.read()
	contents = contents.split('\n')
	urlencoded = []

	for i in contents:
		urlencoded.append(urllib.parse.quote_plus(i))

print('\n'.join(urlencoded))
