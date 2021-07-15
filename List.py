n = int(input("Enter n="))
a = []
s = 0
k = 2*n-1
for i in range(k):
    a.append(float(input()))
print(a)
for i in range(n):
    for j in range(n, k):
        if a[i] < a[j]:
            s += a[j]
    break
print(s)

# n = int(input("Enter n="))
# a = []
# c = 0
# print('a[k] a[k-1] a[k+1]')
# for i in range(n):
#     a.append(int(input()))
# for k in range(n):
#     if (a[k] < (a[k - 1] + a[k + 1]) / 2):
#         c+=1
# print(c)

