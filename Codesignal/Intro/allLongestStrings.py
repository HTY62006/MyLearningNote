def allLongestStrings(inputArray):
    list1 = []
    for i in inputArray:
        a = len(i)
        list1.append(a)
    Max = max(list1)
    list2 = []
    for j in inputArray:
        if len(j) == Max:
            list2.append(j)

    return list2

