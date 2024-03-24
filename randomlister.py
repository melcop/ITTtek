import random

# Oprindelig liste med 5 elementer
original_list = ["A", "B", "C", "D", "E"]

# Tomme lister til at fordele elementer til
list_1 = []
list_2 = []

# Shuffle den oprindelige liste for at blande elementerne
random.shuffle(original_list)

# Fordel elementerne tilfældigt på de to lister
for item in original_list:
    if random.choice([True, False]):  # Tilfældigt valg mellem True og False
        list_1.append(item)
    else:
        list_2.append(item)

# Vis resultatet
print("List 1:", list_1)
print("List 2:", list_2)