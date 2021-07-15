import numpy as np

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("%2.4f" % (matrix[i][j]), end=' ')
        print()

def matrix_max_row(matrix, v):
    max_element = matrix[v][v]
    max_row = v
    for i in range(v + 1, len(matrix)):
        if abs(matrix[v][i]) > abs(max_element):
            max_element = matrix[v][i]
            max_row = i
        if max_row != v:
            matrix[v], matrix[max_row] = matrix[max_row], matrix[v]
        print("Max element", max_element)

def Gauss(matrix):
    v = len(matrix)
    p = 1
    for k in range(v - 1):
        matrix_max_row(matrix, k)
        p*=-1
        for i in range(k + 1, v):
            div = matrix[i][k] / matrix[k][k]
            matrix[i][-1] -= div * matrix[k][-1]
            for j in range(k, v):
                matrix[i][j] -= div * matrix[k][j]
                print_matrix(matrix)
                print(" ")
    if is_singular(matrix):
        print('No solution')
        return

    x = np.zeros(v)
    # зворотній хід
    for k in range(v - 1, -1, -1):
        if matrix[k][k]:
            x[k] = (matrix[k][-1] - sum([matrix[k][j] * x[j] for j in range(k + 1, v)])) / matrix[k][k]
        else:
            x[k] = (matrix[k][-1] - sum([matrix[k][j] * x[j] for j in range(k + 1, v)]))

    det = 1
    print("Gauss method: ")
    for k in range(len(x)):
        print('x[', k + 1, '] =', "%2.4f" % (x[k]), end='\n')
    print(" ")
    print_matrix(matrix)
    for i in range(len(matrix)):
        det *= matrix[i][i]
    print(" ")
    det = p*det
    print("det =", "%2.4f" % (det))
    return x

def is_singular(matrix):
    for i in range(len(matrix)):
        if not matrix[i][i]:
            return True
        return False


matrix = []
file = open("f2.txt", "r")
for line in file:
    matrix.append([float(i) for i in line.split()])

Gauss(matrix)