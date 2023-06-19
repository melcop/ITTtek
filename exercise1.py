a=1
b=2
c=3

if a>b and a>c:
    print("a er det højest nummer")
elif b>a and b>c:
    print("b er det højest nummer")
elif c>a and c>b:
    print("c er det højest nummer")
elif a==b and a>c:
    print("a og b er lige, mens a er større end c")
else:
    print("Alle tre er lige høje")