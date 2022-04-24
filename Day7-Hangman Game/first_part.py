import random

import ASCII_ART
from words import words_list
from ASCII_ART import HANGMANPICS,art
lives=6

#word_list=["ardvark","baboon","camel"]

choice_1=random.choice(words_list)

print(f"The chosen word is {choice_1}")

display=[]
for who in choice_1:
    display.append("_")
print(display)    
    

word_length=len(choice_1)
response=""
while not response:

    user_guess=input("Guess a word:").lower()
####################################
    if user_guess in display:
        print(f"You've already guessed {user_guess}") 

    for position in range(word_length):
        letter=choice_1[position]
        if letter == user_guess:
            display[position]=letter
        
    if user_guess not in choice_1:
        lives-=1
        print("That's not a word , you loose a life")
        if lives==0:
           response=True
           print("You loose")

        
       
    print(display)          

    if "_" not in display:
        response=True
        print("You win") 
    print(HANGMANPICS[lives]) 

    #if display[position]==choice_1[position]:
        #break
