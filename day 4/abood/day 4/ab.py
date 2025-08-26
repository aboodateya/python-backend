list_of_lists = [
    [10, 20, 4, 45, 99, 88],
    [5, 10, 15, 25, 40, 35, 60],
    [3, 2, 1],
    [100, 200, 300, 400, 500]
]
def second_largest(lst):
    if len(lst) < 2:
        return None 
    largest = second = float('-inf') 
    
    for num in lst:
        if num > largest:
            second = largest  
            largest = num     
        elif num > second and num != largest:
            second = num  
    return second

second_largest_list = [second_largest(sublist) for sublist in list_of_lists]

print("Second largest values in each list:", second_largest_list)
