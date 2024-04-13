d = [1, 2]
e = (1, 2)

print(tuple(e))

print(list(d))

print("---------")
d.append(e)
d.insert(1, 11)
print(d)
d.remove(1)
print(d)
d.append("aaa")
print(d)
d.clear()
print(d)