def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        if len(s) >= upperBound:
            found = upperBound
    return found
