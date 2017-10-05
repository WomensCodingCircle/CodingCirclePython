
wanderer_x = 0
wanderer_y = 0
treasure_x = 5
treasure_y = 1
while True:
	direction = eval(input("Which direction would you like to travel in? (N, S, E, or W. done to quit)"))
	if direction == 'E':
		wanderer_x += 1
	elif direction == 'W':
		wanderer_x -= 1
	elif direction == 'N':
		wanderer_y += 1
	elif direction == 'S':
		wanderer_y -= 1
	elif direction == 'done':
		break
	if (wanderer_y == treasure_y and wanderer_x == treasure_x):
		print("Congrats you found a gold necklace!")
		break
print(("You walked to x: " + str(wanderer_x) + " y: " + str(wanderer_y)))
