#Ввести  масив  цілих  чисел.  Елементи  в  першій  половині  масиву  посортувати  за зростанням, а в другій –за спаданням.
n = int(input('Enter n='))
a =[]
k = n//2
for i in range(n):
    a.append(int(input()))
print(a)
print(sorted(a[:k]))
s = a[k:]
s.sort()
print(s[::-1])



