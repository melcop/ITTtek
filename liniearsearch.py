def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [5, 3, 7, 6, 9]
target = 7
result = linear_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print("Element not found")