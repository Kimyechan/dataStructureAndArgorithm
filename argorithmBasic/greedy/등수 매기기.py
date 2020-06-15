# n = int(input())
# expectedRank = []
#
# for _ in range(n):
#     expectedRank.append(int(input()))
#
# expectedRank.sort()
#
# discontent = 0
#
# for i in range(1, len(expectedRank) + 1):
#     discontent += abs(i - expectedRank[i-1])
#
# print(discontent)
n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array.sort()

result = 0
for i in range(1, len(array) + 1):
    result += abs(i - array[i - 1])

print(result)