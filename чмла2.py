def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("%2.4f" %(matrix[i][j]), end=' ')
        print()

def rotation(matrix):
    n = len(matrix)
    for i in range(n-1):
        for j in range(i+1, n):
            c = matrix[i][i] / (matrix[i][i] ** 2 + matrix[j][i] ** 2)**0.5
            s = matrix[j][i]/(matrix[i][i]**2+matrix[j][i]**2)**0.5
            first = [matrix[i][k]*c+matrix[j][k]*s for k in range(len(matrix[i]))]
            second = [-s*matrix[i][k]+matrix[j][k]*c for k in range(len(matrix[i]))]
            for k in range(len(matrix[i])):
                matrix[i][k] = first[k]
                matrix[j][k] = second[k]

    print(" ")
    print("Solved matrix:")
    print_matrix(matrix)

    for i in range(len(matrix)):
        if not matrix[i][i]:
            return "No solution"

    x = [0 for i in range(n)]
    for k in range(n-1,-1,-1):
        x[k] = (matrix[k][-1]-sum([matrix[k][j]*x[j] for j in range(k+1, n)]))/matrix[k][k]

    print(" ")
    for k in range(len(x)):
        print('x[', k + 1, '] =',"%2.4f" %(x[k]), end='\n')

print("Matrix:")
matrix = []
file = open("matrix1.txt", "r")
for line in file:
    matrix.append([int(i) for i in line.split()])
print_matrix(matrix)
rotation(matrix)