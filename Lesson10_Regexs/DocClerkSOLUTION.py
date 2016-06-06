
import re

paragraph = []
found_match = False
# Gold E. Locks (case insensitive, E. or E) Three bears or 3 bears 571 209-4000
patterns = ['gold e\.? locks', 'three bears', '3 bears', '\(?571\)? ?209-?4000']
with open('evidence.txt', 'r') as fh:
	for line in fh:
		if line == '\n':
			if found_match:
				print ''.join(paragraph)
			found_match = False
			paragraph = []

		for pattern in patterns:
			if re.search(pattern, line, re.IGNORECASE):
				found_match = True
		paragraph.append(line)

