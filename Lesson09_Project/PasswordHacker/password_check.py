def check_user_pass(user, password):
	"""
	Checks to see if the user and password are a match
	Returns: True if match, False if not
	"""
	user_pass = {
		'avery': 'rosebud',
		'bruce': 'harley',
		'carla': 'flower',
		'dennis': 'porsche1',
		'eve': 'thunder!',
		'felicity': 'jaguar#1',
		'greta': 'c00l'
	}
	if user_pass[user] == password:
		return True
	else:
		return False

user_list = ['avery', 'bruce', 'carla', 'dennis', 'eve', 'felicity', 'greta']

