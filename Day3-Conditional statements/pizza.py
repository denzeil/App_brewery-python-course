
Response=None
while Response != "":

    print("Welcome to python pizza delivaries")
    size=input("What size do you want? L,M or S: ")
    add_pepperoni=input("Do you want to add pepperoni? Y or N: ")
    extra_cheese=input("Do you want extra cheese? Y or N: ")
    S_P=15
    M_P=20
    L_P=25
    bill=0
    if size=="L":
        print("You have chosen a large sized pizza and it's $",L_P)
        bill=L_P
           
    elif size=="M":
        print("You have chosen a Medium sized pizza and it's $",M_P) 
        bill=M_P

      
    else:
        print("You have chosen a small pizza and it's $",S_P)
        bill=S_P 

    if add_pepperoni=="Y":
        
        if size=="S":
            bill+=2
        else:
            bill+=3
    if extra_cheese=="Y":
        bill+=1               
    print(f"Your bill is ${bill} ")
    input("\nPress enter to continue")
