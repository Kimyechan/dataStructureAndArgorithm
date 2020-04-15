n = int(input())
trophies = list()

for _ in range(n):
    trophies.append(int(input()))

high = 0
canSee = 0

for trophy in trophies:
    if high < trophy:
        high = trophy
        canSee += 1

print(canSee)


trophies.reverse()

high = 0
canSee = 0

for trophy in trophies:
    if high < trophy:
        high = trophy
        canSee += 1

print(canSee)

