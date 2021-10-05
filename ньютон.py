import numpy as np
import matplotlib.pyplot as plt
import math

a = int(input("Input a:"))
b = int(input("Input b:"))
array_x = []
array_y = []
array_x1 = []
array_y1 = []

n = int(input("Enter number of elements : "))
p = np.zeros([n+1, n+2])
value = float(input("Input point for calculating the value of the polynomial: "))

def f(x):
    return (1 / (1 + 25 * (x ** 2)))

def g(x):
    return (math.log(x + 2))

def newton(x,y,n,value):
    #розділені різниці Д
    for i in range(n+1):
        p[i, 0] = x[i]
        p[i, 1] = y[i]

    for i in range(2, n + 2):
         for j in range(n + 2 - i):
             p[j, i] = (p[j + 1, i - 1] - p[j, i - 1]) / (x[j + i - 1] - x[j])
    np.set_printoptions(suppress=True)

    m = p[0][1:]
    lst = []

    #Поліном у формі Ньютона
    t = 1
    for i in range(len(x)):
        t *= (value - x[i])  #(x-x0)(x-x0)(x-x1)
        lst.append(t)
    P = m[0]
    for k in range(1, len(m)):
        P += m[k] * lst[k-1]
    return P

# рівновіддалені вузли
h = (b - a) / n
for i in range(0, n+1):
    v_elem = a + (i * h)
    array_x.append((v_elem))

# Чебишевські вузли
for i in range(0, n+1):
    v_elem1 = (((a + b) / 2) + ((b - a) / 2) * math.cos((((2 * i) + 1) / (2 * (n + 1))) * math.pi))
    array_x1.append(v_elem1)

ch1 = int(input("1-f(x), 2-g(x): "))
if (ch1 == 1):
    # для рівновіддалених
    for i in range(0, n+1):
        array_y.append(f(array_x[i]))

    # для Чебишевських
    for i in range(0, n+1):
        array_y1.append(f(array_x1[i]))

    # для рівновіддалених
    xnew = np.linspace(np.min(array_x), np.max(array_x), 100)
    ynew = [newton(array_x, array_y, n,i) for i in xnew]
    plt.plot(array_x, array_y, 'o', xnew, ynew)
    plt.title("Рівновіддалені вузли")
    plt.grid(True)

    y_new = []
    for i in range(0, 100):
        y_new.append(f(xnew[i]))

    plt.plot(xnew, y_new)
    plt.grid(True)
    plt.show()

    print("The value of polynomial: ", newton(array_x, array_y, n,value))
    print("Pokhybka: ",  (math.fabs(f(value) - newton(array_x, array_y, n,value))))

    # для Чебишевських
    xnew1 = np.linspace(np.min(array_x), np.max(array_x), 100)
    ynew1 = [newton(array_x1, array_y1, n, i) for i in xnew]
    plt.plot(array_x1, array_y1, 'o', xnew1, ynew1)
    plt.grid(True)

    y_new1 = []
    for i in range(0, 100):
        y_new1.append(f(xnew1[i]))

    plt.plot(xnew1, y_new1)
    plt.grid(True)
    plt.title("Чебишевські вузли")
    plt.show()

    print("The value of polynomial: ", newton(array_x1, array_y1,n, value))
    print("Pokhybka: ",  (math.fabs(f(value) - newton(array_x1, array_y1,n, value))))
else:
    # для рівновіддалених
    for i in range(0, n+1):
        array_y.append(g(array_x[i]))

    # для Чебишевських
    for i in range(0, n+1):
        array_y1.append(g(array_x1[i]))

    # для рівновіддалених
    xnew = np.linspace(np.min(array_x), np.max(array_x), 100)
    ynew = [newton(array_x, array_y, n, i) for i in xnew]
    plt.plot(array_x, array_y, 'o', xnew, ynew)
    plt.title("Рівновіддалені вузли")
    plt.grid(True)

    y_new = []
    for i in range(0, 100):
        y_new.append(g(xnew[i]))

    plt.plot(xnew, y_new)
    plt.grid(True)
    plt.show()

    print("The value of polynomial: ", newton(array_x, array_y, n, value))
    print("Pokhybka: ", (math.fabs(g(value) - newton(array_x, array_y, n, value))))

    # для Чебишевських
    xnew1 = np.linspace(np.min(array_x), np.max(array_x), 100)
    ynew1 = [newton(array_x, array_y, n, i) for i in xnew]
    plt.plot(array_x1, array_y1, 'o', xnew1, ynew1)
    plt.grid(True)

    y_new1 = []
    for i in range(0, 100):
        y_new1.append(g(xnew1[i]))

    plt.plot(xnew1, y_new1)
    plt.grid(True)
    plt.title("Чебишевські вузли")
    plt.show()

    print("The value of polynomial: ",  newton(array_x1, array_y1, n, value))
    print("Pokhybka: ", (math.fabs(g(value) - newton(array_x1, array_y1, n, value))))