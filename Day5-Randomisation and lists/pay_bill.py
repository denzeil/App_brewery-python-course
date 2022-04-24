import random
test_seed=int(input("Enter a seed of numbers"))
random.seed(test_seed)

names=input("Give me everybody's names,separated by a comma and space ")
name_pay=names.split(", ")
num_items=len(names)


name_choice=random.randint(0,num_items-1)
person_pay=names[name_choice]
 
print(f"{person_pay} is going to buy the meal today")