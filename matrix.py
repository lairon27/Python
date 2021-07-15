n = int(input("Enter odd n="))
a = []
m = 0
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)

for i in range(n):
    for j in range(n):
        if a[i][j] > m:
            m = a[i][j]
        if m == a[i][j]:
            row_max = i+1
            col_max = j+1
        if i == n//2 and j == n//2:
            row_cen = i+1
            col_cen = j+1
print("max=", m)
print('Row max=', row_max, 'col max=', col_max)
print('Row center=', row_cen, 'col center=', col_cen)

if row_max != row_cen and col_max != col_cen:
    for i in range(n):
        a[i][col_max - 1], a[i][col_cen - 1] = a[i][col_cen - 1], a[i][col_max - 1]
    for j in range(n):
        a[row_max - 1][j], a[row_cen - 1][j] = a[row_cen - 1][j], a[row_max - 1][j]

elif row_max != row_cen and col_max == col_cen:
    for j in range(n):
        a[row_max - 1][j], a[row_cen - 1][j] = a[row_cen - 1][j], a[row_max - 1][j]

elif row_max == row_cen and col_max != col_cen:
    for i in range(n):
        a[i][col_max - 1], a[i][col_cen - 1] = a[i][col_cen - 1], a[i][col_max - 1]
else:
    print("The max element in the center")

for i in a:
    for el in i:
          print(el, end=' ')
    print()