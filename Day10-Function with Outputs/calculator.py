from art import art


# Addition
def add(n1,n2):
    return n1+n2
#subtraction
def sub(n1,n2):
    return  n1-n2
#multiply
def mult(n1,n2):
    return n1*n2
#divide
def div(n1,n2):
    return n1/n2         

operations={"+":add, 
            "-":sub,
            "*":mult,
            "/":div

          }    
def calculator():
    print(art)
    sum1=int(input("Enter your first number"))    
    for i in operations:
        print(i)      
    response=False
    while not response:#This is a flag
        
        
        pick=input("Which operator would you like to use: ")
        

        sum2=int(input("Enter the second number: "))
        func=operations[pick]
        answer=func(sum1,sum2)
        print(f"{sum1} {pick} {sum2} = {answer}\n")

        if_countinue=input(F"Would you like to continue with {answer}? 'yes' or'no' ").lower()
        if if_countinue=="yes":
            sum1=answer
            response=False
        else:
            response=True  
            calculator()#Recursion

calculator()








