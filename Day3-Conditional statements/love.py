from html.entities import name2codepoint


name1=input("What is your name: ").lower()
name2=input("What is her name: ").lower()
name3=name1+name2

count_1=name3.count('t')
count_2=name3.count('r')
count_3=name3.count('u')
count_4=name3.count('e')

unite=count_1+count_2+count_3+count_4


unite_1=name3.count('l')
unite_2=name3.count('o')
unite_3=name3.count('v')
unite_4=name3.count('e')

total=unite_1+unite_2+unite_3+unite_4

string_1=str(unite)+str(total)
int_love=int(string_1)


if int_love<=10 or int_love>=90:
    print(f"Your score is {int_love},you go together like coke and mentos")

elif int_love>40 and int_love<50:
    print(f"Your score is {int_love},you are alright together")

else:
    print(f"Your score is {int_love}")        