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
elif c==0 and b==0:
    print("c og b er lig med nul")
else:
    print("Alle tre er lige høje")

while a>b:
    print("a rules")

while b>c:
    print("b rules")

if a==b or b==c:
    print("bad that all three are the same value!")