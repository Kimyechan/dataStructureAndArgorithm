def scale(sound):
    ascending, descending, mixed = 0, 0, 0

    for index in range(7):
        if sound[index+1] - sound[index] == 1:
            ascending += 1
        elif sound[index+1] - sound[index] == -1:
            descending += 1

    if ascending == 7:
        return "ascending"
    elif descending == 7:
        return "descending"
    else:
        return "mixed"

sound = list(map(int, input().split()))
print(scale(sound))

