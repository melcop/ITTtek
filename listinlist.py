data = [5, "book", [34, "hello"], True]
print(data)
print(data[2])
print(" ---------------- ")
data[0] = 100
print(data)

# For loop
for num in range(5):
    print("Value:{}".format(num))


print("----------------------------------")
# Start, stop, og step for range funktionen
for num in range(2, 10, 2):
    print("Value:{}".format(num))

print("----------------------------------")
a = (10, 20, 30)
b = (40)
print(a)

print("----------------------------------")
k = [57, 38, 43, 64, 25]
k.reverse()
print(k[:3])

print("----------------------------------")
x = {1:"a",2:"b"}
y=x.keys()
print(y) 

print("----------------------------------")
lis = [[8, 7], [6,5]]
result = [p + q for p, q in lis]
print(result)

print("----------------------------------")
# Program to check if a number is prime or not

num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

print("----------------------------------")
s = 1
d = 2    

if s<2:
    print("grow up")
    print(round(1/3, d))