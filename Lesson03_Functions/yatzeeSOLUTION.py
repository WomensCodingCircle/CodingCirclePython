import random

def roll_die():
	return random.randint(1,6)

def yatzee():
	die1 = roll_die()
	die2 = roll_die()
	die3 = roll_die()
	die4 = roll_die()
	die5 = roll_die()
	if die1 == die2 == die3 == die4 == die5:
		print "Yatzee!!"
	return str(die1) + ", " + str(die2) + ", " +str(die3) + ", " +str(die4) + ", " +str(die5) 


print yatzee()
print yatzee()
print yatzee()
print yatzee()
print yatzee()
print yatzee()
print yatzee()
print yatzee()
print yatzee()
print yatzee()
