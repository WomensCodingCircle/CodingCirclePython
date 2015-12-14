budget = raw_input("What is your budget for a car?\n")
try:
    budget = int(budget)
    if (budget > 75000):
        print "You should buy a Tesla!"
    elif (budget < 500):
        print "You are probably better off taking the bus..."
    else:
        print "I don't know, maybe a Toyota Carolla?"
except:
    print "Please be realistic, you can't buy a car on rainbows and love"

print "You can get all your shopping done at Charlotte's Auto Depot!"