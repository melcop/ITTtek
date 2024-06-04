import random

number = random.randint(0, 3)
if number == 2:
    print("Big win!")
elif number == 1:
    print("Small win!")
elif number == 3:
    print("lose!")