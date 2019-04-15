age = int(input("Enter age here: "))
week = int(input("If it is a weekday, enter 1. If it isn't a weekday, enter 2: "))

if age < 18 and week == 1:
	print ("You should go to school!")
elif age >= 18 and week == 1:
	print ("You should go to work!")
elif week == 2:
	print ("Relax: it's the weekend!")
else:
	print ("Insufficient information")