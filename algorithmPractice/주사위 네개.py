maximum = 0
for _ in range(int(input())):
    jusayi = list(map(int, input().split()))
    same = list(set(jusayi))

    jusayi.sort()
    same.sort()

    if len(same) == 1:
        maximum = max(50000+jusayi[0]*5000, maximum)
    elif len(same) == 2:
        if len(set(jusayi[1:3])) == 2:
            maximum = max(maximum, 2000 + (jusayi[1] + jusayi[2]) * 500)
        else:
            maximum = max(maximum, 10000+jusayi[1]*1000)
    elif len(same) == 3:
        result = 0
        for i in range(len(jusayi)-1):
            if jusayi[i] == jusayi[i+1]:
                result = i
        maximum = max(maximum, 1000 + jusayi[result] * 100)
    else:
        maximum = max(maximum, max(jusayi)*100)

print(maximum)