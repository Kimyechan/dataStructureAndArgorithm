# stringArray = input()
#
# count0 = 0
# count1 = 0
#
# if stringArray[0] == '0':
#     count1 = 1
# else:
#     count0 = 1
#
# for i in range(len(stringArray)-1):
#     if stringArray[i] != stringArray[i+1]:
#         if stringArray[i+1] == '0':
#             count1 += 1
#         else:
#             count0 += 1
#
# print(min(count0, count1))
data = int(input())
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))