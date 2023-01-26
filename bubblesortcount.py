def bubbleSortCount(lst):
    #O(n2)time  O(n)space
    comparisons = 0
    exchanges = 0
    for i in range(len(lst)-1,-1,-1):
        for j in range(0,i,1):
            comparisons += 1
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                exchanges += 1
    return (comparisons, exchanges)

print(bubbleSortCount([1, 2, 3, 5, 4, 6, 7])) # (21, 1)
print(bubbleSortCount([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # (45, 45)
print(bubbleSortCount([2, 1, 0, 5, 4])) # (10, 4)