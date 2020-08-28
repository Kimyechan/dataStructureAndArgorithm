# 프로그래밍 연습
# 문제: 정수 4를 1, 2, 3의 조합으로 나타내는 방법은 다음과 같이 총 7가지가 있음
# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
# 정수 n이 입력으로 주어졌을 때, n을 1, 2, 3의 합으로 나타낼 수 있는 방법의 수를 구하시오
# 힌트: 정수 n을 만들 수 있는 경우의 수를 리턴하는 함수를 f(n) 이라고 하면,
# f(n)은 f(n-1) + f(n-2) + f(n-3) 과 동일하다는 패턴 찾기
# 출처: ACM-ICPC > Regionals > Asia > Korea > Asia Regional - Taejon 2001

def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4

    return func(data - 1) + func(data - 2) + func(data - 3)

print(func(5))