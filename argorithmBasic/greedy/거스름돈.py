change = 1000 - int(input())

count = 0

for coin in (500, 100, 50, 10, 5, 1):
    count += change // coin
    change %= coin

print(count)