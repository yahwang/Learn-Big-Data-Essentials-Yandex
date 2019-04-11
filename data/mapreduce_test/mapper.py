#!/usr/bin/env python

from datetime import datetime
import re
import sys

def mapper():
	tld = "http://www.theassociates.co.uk"
	pattern = '^([\d.]+) ([\w-]+) ([\w-]+) \[(.+)\] \"(.+)\" (\d{3}) (\d+)$'
	for line in sys.stdin:
		result = re.match(pattern, line)
		if result is None:
			continue
		time_str, request = result.group(4), result.group(5)
		try:
			method, resource, protocol = request.split(" ")
		except ValueError:
			continue

		# Need to convert to ordinal because we want to sort by day
		time_dt = datetime.strptime(time_str.split(" ")[0], "%d/%b/%Y:%X")
		time_ordinal = time_dt.toordinal()

		if resource.startswith(tld):
			resource = resource[len(tld):]

		if resource == "/":
			print("{}\t1".format(time_ordinal))

if __name__ == "__main__":
	mapper()
