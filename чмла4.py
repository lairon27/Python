import numpy as np

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

def SP(matrix, e):
    y0 = np.ones(len(matrix))
    s0 = sum([x*x for x in y0])
    y0_norm = s0 ** (1/2)
    xk = y0 / y0_norm
    k, lamb_p, lamb_k = 0, 0, 0
    while True:
        k += 1
        y_k = np.dot(matrix, xk)
        s_k = sum([x * x for x in y_k])
        t_k = sum([x * y for y, x in zip(y_k, xk)])
        yk_norm = s_k ** (1/2)
        xk = y_k / yk_norm
        lamb_p = lamb_k
        lamb_k = s_k / t_k
        print(f"\nIteration: {k}\nLambda: {lamb_k}\t{y_k}")
        if abs(lamb_k - lamb_p) <= e:
            break

print("Matrix:")
matrix = []
file = open("matrix0.txt", "r")
for line in file:
    matrix.append([int(i) for i in line.split()])

print_matrix(matrix)
SP(matrix, 0.001)