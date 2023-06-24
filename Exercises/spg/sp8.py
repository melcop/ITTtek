import sys
# pass 1 and 2 as argv
s = sys.argv[1]
bi = sys.argv[2]
he = sys.argv[3]
    
print(type(bi))
bi, he = int(bi), int(he)

def main(b, c):
    d = b * c
    print(bin(d))
    print(hex(d))
    return d

def p():
    ps = main(bi, he) 
    u(ps)

def u(pa):
    i = 10
    while i > 0:  
        val = pa ** i
        print(f"dec : {val} bin: {bin(val)} hex: {hex(val)}")
        i -= 1

p()