def matrixElementsSum(matrix):
    k = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[j][i] != 0:
                k += matrix[j][i]
            else:
                break
    return k
