import random, time

p = random.randint(1,1000)
print(p)
time.sleep(10)

#q = input()
#p = int(q)
for x in range(p):
    for y in range(p):
        for z in range(p):
            print(x, y, z)

print("Try with threads")