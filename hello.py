print("Hello")
a=1
print(a)
b=0
print(a+b)
print(a-b)
b=2
print(a//b)
print(b//a)
print(a//a)
print(b//b)
print(a//b//b)

d = {'Milk': 1, 'Soap': 2, 'Towel': 3}
if 'Soap' in d:
    print(d['Soap'])
print(d.get(2))
print(d.get('Milk'))
print(d.pop('Soap'))
print(d)