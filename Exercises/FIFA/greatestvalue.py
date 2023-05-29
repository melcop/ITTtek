def find_greatest(lst):
    if not lst:
        return None
    
    greatest = lst[0]
    
    for num in lst:
        if num > greatest:
            greatest = num
            
    return greatest

elements = input("Enter the elements of the list (space-separated): ").split()
my_list = [int(elem) for elem in elements]

result = find_greatest(my_list)
print(my_list, sep= ",")
print("the greatest element in the list is:", result)