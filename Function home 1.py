A = int(input("Enter A="))
B = int(input("Enter B="))
n = int(input("Enter N="))
for k in range(n):
    for m in range(n):
        if(k*A+m*B)<n:
            print('k =',k, '\t', 'm =',m, '\t', 'k*A+m*B =',k*A+m*B)