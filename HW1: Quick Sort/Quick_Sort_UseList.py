def QuickSort(x):
    equal = []
    left = []
    right = []
    # 如果list長度<=1，則不必排序。
    if len(x) <= 1:
        return x
    else:
        # 設位於[0]的值為pivot
        pivot = x[0]
    for i in x:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)
    left = QuickSort(left) #對left進行quick sort
    right = QuickSort(right) # 對right進行quick sort
    correct = left+equal+right # 排序好的list
    return correct
    
    example = [34,21,5,9,0,12,-3,-15]
    QuickSort(example)
