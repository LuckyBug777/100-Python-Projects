#Project Of day 2 Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
number_of_people = int(input("How many people to split the bill? "))
print("Each person should pay: $" + str(round((bill * tip/100 + bill)/number_of_people,2)))
print(f"Each person should pay: ${round((bill * tip/100 + bill)/number_of_people,2)}")
