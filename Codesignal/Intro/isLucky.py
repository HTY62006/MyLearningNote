def isLucky(n):
    l = len(str(n))/2
    first = int(n//10**l)
    second = int(n%10**l)
    s1 = 0
    s2 = 0
    for d1 in str(first):
        s1+=int(d1)
    for d2 in str(second):
        s2+=int(d2)
    if s1 == s2:
        return True
    else:
        return False
    

