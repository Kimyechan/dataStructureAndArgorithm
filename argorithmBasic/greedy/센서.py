import sys

n = int(input())
k = int(input())

array = []

array= list(map(int, input().split(' ')))

if k >= n:
    print(0)
    sys.exit()

array.sort(reverse=True)

distance = []
for i in range(n-1):
    distance.append(array[i] - array[i+1])

distance.sort(reverse=True)

for i in range(k-1):
    distance[i] = 0

print(sum(distance))