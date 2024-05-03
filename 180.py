x = {"a": 1, "b" : 2, "d": 5}
y = {"b": 3, "c" : 4}
z = {**x, **y}

print(z)

s = []
s.append(2)
print(s)

print("-------")
s.append(z)
print(s)
print("-------")
s.append(s)
print(s)