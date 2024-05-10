dep = []

dep.append(300)
dep.append(200)
dep.append("abe")


print(dep.index("abe"))
print("----------")
dep.append("aaa")
print(dep)

print(dep.count(200))

dap = []

dap.append(100)
dap.append(150)
dap.append("ccc")
dap.insert(3, "abe")
print("----------")
print(dap)
print("----------")
dep.append(dap.append(dep))
print(dep)
