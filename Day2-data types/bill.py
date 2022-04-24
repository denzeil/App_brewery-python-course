print("Welcome to the tip program")
bill=int(input("What was the total bill? $" ))
tip=int(input("What percentage would you like to give? 10,12 or 15?"))
split=int(input("How many people to split the bill?"))


bill_2=bill*((tip/100)+1)

split_2=bill_2/split

print("Each person should pay: ",round(split_2,2),"$")

