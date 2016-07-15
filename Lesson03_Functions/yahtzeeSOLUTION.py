import random

def roll_die():
    # Returns a random integer from 1 - 6
	return random.randint(1,6)

def yahtzee():
    # Rolls 5 dice and if all are equal prints yahtzee. 
    # Returns a string containg all values of the dice
	die1 = roll_die()
	die2 = roll_die()
	die3 = roll_die()
	die4 = roll_die()
	die5 = roll_die()
	if die1 == die2 == die3 == die4 == die5:
		print "Yahtzee!!"
	return str(die1) + ", " + str(die2) + ", " +str(die3) + ", " +str(die4) + ", " +str(die5) 


# Calls yahtzee 10 times
print yahtzee()
print yahtzee()
print yahtzee()
print yahtzee()
print yahtzee()
print yahtzee()
print yahtzee()
print yahtzee()
print yahtzee()
print yahtzee()
