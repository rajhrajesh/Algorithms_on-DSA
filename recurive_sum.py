def recursive_sum(arr):
    if len(arr) == 0:
        return 0 
    return arr[0] + recursive_sum(arr[1:])

numbers = [2,4,6,11]
print(recursive_sum(numbers))

# 2 programm'
def recursive_count(arr):
    if len(arr) == 0:
        return 0 
    return 1 + recursive_count(arr[1:])

numbers = [12,3,4,5,6]
print(recursive_count(numbers))

# 3 programm' 
def recursive_max(arr):
    if len(arr) == 1:
        return arr[0]
    max_rest = recursive_max(arr[1:])
    return arr[0] if arr[0] > max_rest else max_rest 
arr = [12,3,4,5,6]
print(recursive_max(arr))