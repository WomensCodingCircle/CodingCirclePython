adjectives = {
	'A': 'Acceptable',
	'B': 'Baggy',
	'C': 'Caluclating',
	'D': 'Dimwitted',
	'E': 'Empty',
	'F': 'Filthy',
	'G': 'Greedy',
	'H': 'Harsh',
	'I': 'Impure',
	'J': 'Jaded',
	'K': 'Klutzy',
	'L': 'Lazy',
	'M': 'Meek',
	'N': 'Negative',
	'O': 'Odd',
	'P': 'Prickly',
	'Q': 'Queasy',
	'R': 'Rude',
	'S': 'Scaly',
	'T': 'Thick',
	'U': 'Unruly',
	'V': 'Vapid',
	'W': 'Worthless',
	'X': 'Xenophobic',
	'Y': 'Yellowish',
	'Z': 'Zany'
}


def acrostic(name):
	name = name.upper()
	for letter in name:
		current_adj = adjectives[letter]
		print(("{0}-{1}".format(letter, current_adj)))


acrostic('Charlotte')
