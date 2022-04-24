n=int(input("Input your nuumber: "))
def prime_checker(number):
    prime=True
    for i in range(2,number-1):
        
        if number%i==0:
            prime=False
            
    if prime:        
        print("Ït's a prime number")
    else:
        print("It's not a prime number")    


prime_checker(number=n)        
