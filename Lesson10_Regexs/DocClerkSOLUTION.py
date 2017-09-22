
import re

# Initialize an empyt paragraph
paragraph = []
found_match = False
# These are the regexs that we are going to use
#    Gold E. Locks (case insensitive, E. or E) Three bears or 3 bears 571 209-4000
patterns = ['gold e\.? locks', 'three bears', '3 bears', '\(?571\)? ?209-?4000']
with open('evidence.txt', 'r') as fh:
    for line in fh:
        # If it is the end of a paragraph, 
        # print the paragraph if we found a match to the regex
        if line == '\n':
            if found_match:
                print((''.join(paragraph)))
            # Reset found_match and paragraph for the next paragraph
            found_match = False
            paragraph = []
        
        # seach each pattern, and if there is a match, set found_match flag to True
        for pattern in patterns:
            if re.search(pattern, line, re.IGNORECASE):
                found_match = True
        # Append line to paragraph
        paragraph.append(line)

