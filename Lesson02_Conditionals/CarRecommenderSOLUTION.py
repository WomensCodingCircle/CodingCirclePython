# Ask get budget for car from user
budget = raw_input("What is your budget for a car?\n")
try:
    # raw_input returns a string and we need a number so convert to int
    budget = int(budget)
    if (budget > 75000):
        print "You should buy a Tesla!"
    elif (budget < 500):
        print "You are probably better off taking the bus..."
    else:
        print "I don't know, maybe a Toyota Corolla?"
# This will execute if the budget can't be converted to an int
except:
    print "Please be realistic, you can't buy a car on rainbows and love"
# This will execute no matter what
print "You can get all your shopping done at Charlotte's Auto Depot!"