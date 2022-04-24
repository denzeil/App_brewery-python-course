import random
# Rock Paper Scissors ASCII Art
print("Type 0 for rock,1 for paper and 2 for scissors")
# Rock
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
value=int(input("Choose :"))

map=[rock,paper,scissors]
human=map[value]
print("You chose: ",human )

comp_value=random.randint(0,2)

value2=map[comp_value]
print("The computer chose: ",value2)


if (value>=3 or value<0):
    print("Enter a valid number")
elif (value==2 and comp_value==1):
    print("You Win\n")
elif (value==2 and comp_value==0):
    print("You win")
elif (value==0 and comp_value==2):
    print("You win")
elif value==comp_value:

    print("It's a draw")    
else:
    print("You loose!")
    

