 def alternatingSums(a):
    s1 = 0
    s2 = 0
    for i in range(len(a)):
        if i%2 == 0:
            s1+=a[i]
        elif i%2 == 1:
            s2+=a[i]
    return [s1, s2]
