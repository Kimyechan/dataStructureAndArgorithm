n = int(input())
expectedRank = []

for _ in range(n):
    expectedRank.append(int(input()))

expectedRank.sort()

discontent = 0

for i in range(1, len(expectedRank) + 1):
    discontent += abs(i - expectedRank[i-1])

print(discontent)