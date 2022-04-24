height=float(input("Enter your height: "))
weight=int(input("Enter your weight: "))

BMI=weight/height**2

value=round(BMI,1)
if (value<=18.5):
    print("You are overweight")
elif(value>18.5 and value<=25):
    print("You have a normal weight")    

elif(value>25 and value<=30):
    print("You are overweight") 

elif(value>30 and value<=35):
    print("You are obese") 

else:
    print("You are clinically obese")         