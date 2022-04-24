import random
test_seed=int(input("Create a seed number: "))
random.seed(test_seed)
head_t=random.randint(0,1)
if head_t==1:
    print("Heads")
else:
    print("Tails")    