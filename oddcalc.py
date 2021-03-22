numone = input("Give me a number: ")
numtwo = input("Give me another number: ")
expression = input("To multiply enter mul, to divide enter div and for Modulo enter mod: ")

if (expression == "mul"):
	output = int(numone)*int(numtwo)
	print("The answer is: " + str(output))

elif (expression == "div"):
	output = int(numone)/int(numtwo)
	print("The answer is: " + str(output))

elif (expression == "mod"):
	output = int(numone)%int(numtwo)
	print("The answer is: " + str(output))

else:
	print("Sorry I don't understand")