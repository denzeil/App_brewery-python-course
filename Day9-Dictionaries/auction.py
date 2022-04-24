
from art import art
auction={}
print(art)
response=False
while not response:
    name=input("What is your name: ")
    price=int(input("What price do you bid$ "))
    auction[name]=price
    other=input("Are there any other bidders,yes or no: ").lower()
    if other=="yes":
        response=False
    else:
        response=True
print(auction)  
current_values=auction.values()
max_value=max(current_values)
print(max_value)
      
