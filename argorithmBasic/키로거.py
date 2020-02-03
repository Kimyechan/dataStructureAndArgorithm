# from sys import stdin
#
# stack1 = []
# stack2 = []
# location = 0
#
# test_case = int(input())
#
# for _ in range(test_case):
#     password = stdin.readline()
#
#     for index in range(len(password)):
#         if stack1 == None and (password[index] == '<' or password[index] == '>' or password[index] == '-'):
#             continue
#
#         if len(stack1) == location + 1:
#             for _ in range(len(stack2)):
#                 stack1.append(stack2.pop())
#         else:
#             while len(stack1) == location + 1:
#                 stack2.append(stack1.pop())
#
#         if location < 0:
#             location = 0
#
#         if password[index] != '<' and password[index] != '>' and password[index] != '-':
#             stack1.append(password[index])
#             location += 1
#         elif password[index] == '<':
#             location -= 1
#         elif password[index] == '>':
#             location += 1
#         elif password[index] == '-':
#             stack1.pop()
#
#     for index in range(len(stack1)):
#         print(stack1[index], end='')
#
#     stack1.clear()
#     stack2.clear()
test_case = int(input())

for _ in range(test_case):
    left_stack = []
    right_stack = []
    data = input()
    for i in data:
        if i in data:
            if i == '-':
                if left_stack:
                    left_stack.pop()
            elif i == '<':
                if left_stack:
                    right_stack.append(left_stack.pop())
            elif i == '>':
                if right_stack:
                    left_stack.append(right_stack.pop())
            else:
                left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))
















