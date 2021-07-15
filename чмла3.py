import numpy as np

def isDDM(m, n):
    for i in range(0, n):
        sum = 0
        for j in range(0, n):
            sum = sum + abs(m[i][j])

        sum = sum - abs(m[i][i])

        if (abs(m[i][i]) < sum):
            return False

    return True

def seidel(A, b, eps):
    n = len(A)
    x = np.zeros(n)

    converge = False
    Iteration = 0
    if ((isDDM(A, n))):
        while not converge:
            x_new = np.copy(x)
            for i in range(n):
                s1 = sum(A[i][j] * x_new[j] for j in range(i))
                s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
                x_new[i] = (b[i] - s1 - s2) / A[i][i]

            converge = np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
            Iteration += 1
            x = x_new
        print('Кількість ітерацій :', Iteration)
        print('Кількість ітерацій :', x)
        return x
    else:
        return "Не розв'язується"


A = np.array([[4, -1, -1, 0],
           [-1, 4, 0, -1],
           [-1, 0, 4, -1],
           [0, -1, -1, 4]])

b = np.array([2, 2, 2, 2])
eps = 0.1
print('Рішення :', seidel(A, b, eps))