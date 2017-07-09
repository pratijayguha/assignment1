import random
def roll_dice(m,n):
    for i in range(m):
        print(random.randint(1,n))
    print("That's all!")
