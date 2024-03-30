dep = []

dep.append(300)
dep.append(200)
dep.append('abe')


print(dep.index("abe"))
print("----------")
dep.append('aaa')
print(dep)

print(dep.count(200))