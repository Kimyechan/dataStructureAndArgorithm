bird = int(input())

time = 0
count = 1

while bird > 0:
    if bird >= count:
        bird -= count
        count += 1
        time += 1
    else:
        count = 1

print(time)
