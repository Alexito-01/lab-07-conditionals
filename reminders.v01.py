hour = input("What is the current hour in military time(0-23): ")

if int(hour) <=5:
	print("It’s early. You should be sleeping!")

elif int(hour) <=7:
	print("Wake up, brew that coffee, get that mile run in, and get that breakfast…")

elif int(hour) <=9:
	print("Time to go to work.")

elif int(hour) <=12:
	print("You should be working!")

elif int(hour) <=13:
	print("Take your lunch break!")

elif int(hour) <=17:
	print("Do you feel that afternoon lull?")

elif int(hour) <=19:
	print("Time to hit the gym…")

elif int(hour) <=21:
	print("Gotta eat that dinner.")

elif int(hour) <=23:
	print("Get that SLEEP. And rePEAT!")

else:
	print("You didn’t type an acceptable value! (0-23)")