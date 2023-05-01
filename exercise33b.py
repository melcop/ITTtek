numbers = []

def test(max, incr):
    i = 0
    while i < max:
        print(f"At the top i is {i}")
        numbers.append(i)
    
        i = i + incr
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
    

test(6, 2)
print("The numbers: ")
for num in numbers:
    print(num)