#First of all, some greetings to the user, after that ask the data

print("welcome to the bill calculator\n")
value = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? %"))
people = int(input("How many people to split the bill? "))

#now that the main variables are defined, we are gonna do the math part

calculated_tip = (value/people)*tip/100
bill = (value/people) + calculated_tip
rounded_bill = round(bill,2)

#Print the result to the user

print(f"Each person should pay ${rounded_bill}")