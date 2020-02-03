# def stackSequence(sequence):
#     stack = []
#     outPrint = []
#     num = 1
#     plusCount, minusCount = 0, 0
#     index = 0
#
#     while True:
#         if stack[-1] != sequence[index] or stack == None:
#             stack.append(num)
#             num += 1
#             plusCount += 1
#             outPrint.append("+")
#         elif stack[-1] == sequence[index]:
#             index += 1
#             stack.pop()
#             minusCount += 1
#             outPrint.append("-")
#
#         if minusCount == len(sequence):
#             return outPrint
#
#         if plusCount == len(sequence) and stack[len(stack)-1] != sequence[index]:
#             outPrint.clear()
#             outPrint.append("NO")
#             return outPrint
#
# count = int(input())
# sequence = list()
#
# for index in range(count):
#     num = int(input())
#     sequence.append(num)
#
# print(stackSequence(sequence))
n = int(input())

count = 1
stack = []
result = []

for i in range(1, n+1):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(result))



