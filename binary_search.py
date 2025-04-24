def binary_search(list, item):
    low = 0  # new low is now 3
    high = len(list) -1 # 5 -1 = 4
    mid = (low + high) / 2   # 4/2 = 2, new 3 + 4 / 2 = 7/2 = 3

    while low <= high:   #0 <= 2 , 3 <= 4
        mid = (low + high) # 0 + 2  = 2 , 3 + 4 = 7
        guess = list[mid] # pos-> index is 2 , pos -> index is 

        if guess == item: # 2 != 3 
            return mid
        if guess > mid: #
            high = mid - 1
        else:
            low = mid + 1 
my_list = [1,3,4,5,6]

print(binary_search(my_list, 5))