import random
print(min(max(False, -3, -4), 2, 7))

print("----------------------------")

a = set()
for n in range(21, 40):
    if n % 2 ==0:
        a.add(n)
print(a)
print("----------------------------")


for _ in range(5):  # Skifter "5" ud med det ønskede antal tilfældige tal
    random_number = random.randint(1, 100)
    print(random_number)