def bubbleSort(the_list):
    for i in range(len(the_list)-1, -1, -1):
        for j in range(0, i, 1):
            if the_list[j] > the_list[j+1]:
                the_list[j], the_list[j+1] = the_list[j+1], the_list[j]
    return the_list

print(bubbleSort([5, 3, 10, 6, 1])) # [1, 3, 5, 6, 10]
print(bubbleSort([100, 98, 101, 10])) # [10, 98, 100, 101]
print(bubbleSort([2, 1, 0, 5, 4])) # [0, 1, 2, 4, 5]