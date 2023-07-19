import random, time

p = random.randint(220,1000)
print(p)
time.sleep(10)
x = random.randint(25,100)
y = random.randint(30,110)
z = random.randint(40,120)
#q = input()
#p = int(q)
for x in range(p):
    for y in range(p):
        for z in range(p):
            print(x, y, z)


#print("Try with threads")