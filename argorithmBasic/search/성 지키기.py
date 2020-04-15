n, m = map(int, input().split())

array = list()

for _ in range(n):
    array.append(input())

row = [0] * n
column = [0] * m

for i in range(n):
    for j in range(m):
        if array[i][j] == 'X':
            row[i] = 1
            column[j] = 1

rowCount = 0
columnCount = 0

for i in range(n):
    if row[i] != 1:
        rowCount += 1

for j in range(m):
    if column[j] != 1:
        columnCount += 1

if rowCount >= columnCount:
    print(columnCount + rowCount - columnCount)
else:
    print(rowCount + columnCount - rowCount)