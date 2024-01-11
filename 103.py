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
    random_number2 = random.randint(1, 100) * 2
    print(random_number)
    print("gange 2: ", random_number2)
    
print("----------------------------") 

def fun(x, y):
    if x == 0:
        return y
    else:
        return fun(x-1, x * y)
print(fun(4,2))
print("----------------------------") 
s = set('CLC')
t = list(s)
t =t[::-1]
print(t)

print("----------------------------") 
p='Love for coding'
print(p[4],p[5])

print("----------------------------") 
aList = ["Coding", [4, 8, 12, 16]]
print(aList[1][3])

print("----------------------------") 
dict_a = {"eggs": 1.50, "milk": 1.2, "bacon": 2.99}
dict_b = {"bread": 2.20, "jam": 4.87}
dict_c = {}

print(len(dict_a))


print("----------------------------") 
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

print("----------------------------")
a=15
b=10
print(a)
result = a if a < b else b
print(result)
a=b
print(b)