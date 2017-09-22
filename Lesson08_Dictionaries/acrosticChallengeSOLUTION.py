import random

adjectives = {
	'A': ['Adorable', 'Awesome', 'Acceptable'],
	'B': ['Baggy', 'Bad'],
	'C': ['Caluclating', 'Cheerful'],
	'D': ['Dimwitted', 'Dull', 'Defiant'],
	'E': ['Empty', 'Earnest'],
	'F': ['Famous',  'Feisty', 'Filthy'],
	'G': ['Greedy', 'Gentle'],
	'H': ['Healthy', 'Harsh'],
	'I': ['Innocent', 'Infinite', 'Impure'],
	'J': ['Joyous', 'Jaded'],
	'K': ['Kind', 'Klutzy'],
	'L': ['Lazy', 'Likable', 'Little'],
	'M': ['Meek', 'Marvelous'],
	'N': ['Nice', 'Nocturnal', 'Negative'],
	'O': ['Opulent', 'Odd'],
	'P': ['Popular', 'Poor', 'Prickly'],
	'Q': ['Queasy', 'Quick'],
	'R': ['Rude', 'Reasonable', 'Rich'],
	'S': ['Scaly', 'Silly', 'Scholarly'],
	'T': ['Thick', 'Tepid', 'Tough'],
	'U': ['Unruly', 'Unique'],
	'V': ['Vapid', 'Virtuous', 'Vital'],
	'W': ['Worthless', 'Weak', 'Warm'],
	'X': ['Xenophobic'],
	'Y': ['Yellowish', 'Young', 'Yummy'],
	'Z': ['Zany', 'Zealous']
}


def acrostic(name):
	name = name.upper()
	for letter in name:
		rand_idx = random.randint(0, len(adjectives[letter]) - 1)
		current_adj = adjectives[letter][rand_idx]
		print(("{0}-{1}".format(letter, current_adj)))


acrostic('Charlotte')
