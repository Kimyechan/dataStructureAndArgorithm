jusayi = list(map(int, input().split()))
same = list(set(jusayi))

jusayi.sort()
same.sort()

if len(same) == 1:
    print(10000+jusayi[0]*1000)
elif len(same) == 2:
    i = 0
    while jusayi[i] == same[i]:
        i += 1
        if i == 2:
            break
    print(1000+jusayi[i]*100)
else:
    print(max(jusayi)*100)