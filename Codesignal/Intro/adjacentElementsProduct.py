def adjacentElementsProduct(inputArray):
    list1 = []
    for i in range(len(inputArray)):
        if i+1 < len(inputArray):
            n = inputArray[i]*inputArray[i+1]
            list1.append(n)
    return max(list1)

