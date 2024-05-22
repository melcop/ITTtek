x = [1, 2, 3]
y = [4, 5, 6]
z =  [x, y]
print(z[0][1], z[1][2])
print(z)
print("----------------")
z.append(24)
z.extend("as")
z.remove(x)
print(z)

print("--------------------------")
lst = ['P', 20, 'Q', 4.5]
item = iter(lst)
lst.append(23)
print(next(item))
print(lst)
lst.clear()
print(lst)
