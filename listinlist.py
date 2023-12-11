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