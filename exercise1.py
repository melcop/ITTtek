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
elif a==c and a>b:
    print("a er lig med c og større end b")
elif c==b and c>a:
    print("c er lig med b og c er større end a")
else:
    print("Alle tre er lige høje")