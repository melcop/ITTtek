numbers = []

def test(s):
    i = 0
    while i < s:
        print(f"At the top i is {i}")
        numbers.append(i)
    
        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
    

test(6)
print("The numbers: ")
for num in numbers:
    print(num)