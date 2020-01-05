def sortByHeight(a):
    list1 = []
    list2 = []
    for i in range(len(a)):
        if a[i] != -1:
            list1.append(a[i])
            list2.append(i)
    list1.sort()
    k = 0
    while k<len(list1):
        for j in list2:
            a[j] = list1[k]
            k+=1
    return a
