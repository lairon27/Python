import numpy as np
import matplotlib.pyplot as plt
import math

a=int(input("Input a:"))
b=int(input("Input b:"))
array_x=[]
array_x1=[]
array_y=[]
array_y1=[]

n = int(input("Enter number of elements : "))
value = float(input("Input point for calculating the value of the polynomial: "))

def f(x):
    return(1/(1+25*(x**2)))

def g(x):
    return(math.log(x+2))

#рівновіддалені вузли
for i in range(0, n + 1):
    v_elem=a+(i*(b-a)/n)
    array_x.append((v_elem))

#Чебишевські вузли
for i in range(0,n+1):
    v_elem1=(((a+b)/2)+((b-a)/2)*math.cos((((2*i)+1)/(2*(n+1)))*math.pi))
    array_x1.append(v_elem1)

ch1=int(input("1-f(x), 2-g(x): "))
if(ch1==1):

    #для рівновіддалених
    for i in range(0, n+1):
        array_y.append(f(array_x[i]))

    #для Чебишевських
    for i in range(0,n+1):
        array_y1.append(f(array_x1[i]))

    def lagrange(x,y,t):
        z=0
        for j in range(len(y)):
            p1=1; p2=1
            for i in range(len(x)):
                if i!=j:
                    p1=p1*(t-x[i])
                    p2=p2*(x[j]-x[i])
            z+=y[j]*p1/p2
        return z

    #для рівновіддалених
    xnew=np.linspace(np.min(array_x),np.max(array_x),100)
    ynew=[lagrange(array_x,array_y,i) for i in xnew]
    plt.plot(array_x,array_y,'o', xnew, ynew)
    # plt.plot(xnew, ynew, '-')
    plt.title("Рівновіддалені вузли")
    plt.grid(True)

    y_new=[]
    for i in range(0, 100):
        y_new.append(f(xnew[i]))

    plt.plot(xnew,y_new)
    plt.grid(True)
    plt.show()

    print("The value of polynomial: ",lagrange(array_x,array_y,value))
    print("Pokhybka: ",(math.fabs(f(value)-lagrange(array_x,array_y,value))))


    #для Чебишевських
    xnew1=np.linspace(np.min(array_x1),np.max(array_x1),100)
    ynew1=[lagrange(array_x1,array_y1,i) for i in xnew1]
    plt.plot(array_x1,array_y1,'o',xnew1,ynew1)
    plt.grid(True)

    y_new1=[]
    for i in range(0, 100):
        y_new1.append(f(xnew1[i]))

    plt.plot(xnew1,y_new1)
    plt.grid(True)
    plt.title("Чебишевські вузли")
    plt.show()

    print("The value of polynomial: ",lagrange(array_x1,array_y1,value))
    print("Pokhybka: ",(math.fabs(f(value)-lagrange(array_x1,array_y1,value))))

else:

    # для рівновіддалених
    for i in range(0, n+1):
        array_y.append(g(array_x[i]))

    # для Чебишевських
    for i in range(0, n+1):
        array_y1.append(g(array_x1[i]))


    def lagrange(x, y, t):
        z = 0
        for j in range(len(y)):
            p1 = 1
            p2 = 1
            for i in range(len(x)):
                if i != j:
                    p1 = p1 * (t - x[i])
                    p2 = p2 * (x[j] - x[i])
            z += y[j] * p1 / p2
        return z


    # для рівновіддалених
    xnew = np.linspace(np.min(array_x), np.max(array_x), 100)
    ynew = [lagrange(array_x, array_y, i) for i in xnew]
    plt.plot(array_x, array_y, 'o', xnew, ynew)
    plt.title("Рівновіддалені вузли")
    plt.grid(True)

    y_new = []
    for i in range(0, 100):
        y_new.append(g(xnew[i]))

    plt.plot(xnew, y_new)
    plt.grid(True)
    plt.show()

    print("The value of polynomial: ", lagrange(array_x, array_y, value))
    print("Pokhybka: ", (math.fabs(g(value) - lagrange(array_x, array_y, value))))

    # для Чебишевських
    xnew1 = np.linspace(np.min(array_x1), np.max(array_x1), 100)
    ynew1 = [lagrange(array_x1, array_y1, i) for i in xnew1]
    plt.plot(array_x1, array_y1, 'o', xnew1, ynew1)
    plt.grid(True)

    y_new1 = []
    for i in range(0, 100):
        y_new1.append(g(xnew1[i]))

    plt.plot(xnew1, y_new1)
    plt.grid(True)
    plt.title("Чебишевські вузли")
    plt.show()

    print("The value of polynomial: ",  lagrange(array_x1, array_y1, value))
    print("Pokhybka: ",  (math.fabs(g(value) - lagrange(array_x1, array_y1, value))))