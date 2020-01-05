def makeArrayConsecutive2(statues):
    MIN = min(statues)
    MAX = max(statues)
    total = MAX-MIN+1
    dif = total - len(statues)
    return dif

