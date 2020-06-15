N, QuizOX = int(input()), input()

bonus = 0
score = 0

for num in range(1, len(QuizOX)+1):
    if QuizOX[num-1] == 'O':
        if num != 1 and QuizOX[num-2] == QuizOX[num-1]:
            bonus += 1
            score = score + num + bonus
        else:
            score += num
    else:
        bonus = 0

print(score)