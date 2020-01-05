def commonCharacterCount(s1, s2):
    dict1 = {}
    for i in s1:
        dict1[i] = s1.count(i)
    dict2 = {}
    for j in s2:
        dict2[j] = s2.count(j)
    a = dict1.keys() & dict2.keys()
    list1 = []
    for k in a:
        if dict1[k] >= dict2[k]:
            list1.append(dict2[k])
        else:
            list1.append(dict1[k])
    return sum(list1)
        
            

