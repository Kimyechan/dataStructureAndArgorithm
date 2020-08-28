<script type="text/javascript" 
src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML">
</script>


# 소수 체크와 소인수 분해

- 인수, 소수, 소인수개념
    - 인수: 수의 약수
    - 소수: 약수가 1과 자기자신
    - 소인수: 인수중 소수인 것
    - 소인수분해: 수를 소인수의 곱으로만 나타낸 것
    
- 소수 체크는 반복문으로 진행하면 X
- 소인수분해의 경우 조금의 트릭으로 진행
- 두 알고리즘 모두  $$ O(\sqrt(N))$$ 

```python
    # 소수 체크 기본
    # (prime_check 말고 isPrime 등의 관용적인 함수명을 사용)
    def prime_check(N):
        for i in range(2, N):
            if N%i==0: return False
            if i*i > N: break
        return True

    # 소인수분해 기본
    def prime_factorization(N):
        p, fac = 2, []
        while p**2 <= N:
            if N%p==0:
                N //= p
                fac.append(p)
            else:
                p += 1
        if N > 1 : fac.append(N)
        return fac
```

- 위의 알고리즘은 단 한 번 사용하거나 빠르게 체크할 때는 좋지만 여러 쿼리를 묻는 문제등의 경우 시간복잡도가 크다
- 이런 문제를 해결하기 위해 소수 리스트를 미리 만드는 방법인 __에라토스테네스의 체__가 있다

```python
    #에라토스테네스의 체를 활용한 소수 리스트 구하기
    def era_prime(N):
        A, p = [0 for _ in range(N+1)], []
        for i in range(2, N):
            if A[i] == 0 : p.append(i)
            else: continue
            for j in range(i**2, N, i):
                A[j] = 1
        return p
```  

이런 리스트를 만들면 소인수분해도 다음과 같이 가능하다

```python
    # 소수 리스트가 있는 경우 소인수 분해
    # 소수 리스트의 그키가는 sqrt(N)보다 커야함
    def prime_factorization_2(N, p):
        fac = []
        for i in p:
            if N == 1 or N > i*i : break
            while N%i == 0:
                fac.append(i)
                N //= i
            return fac
```

- 활용의 예
    - 소인수의 개수
    - 소인수의 합
    - 소인수분해를 위한 또 하나의 트릭

```python
# 활용 1 : 소인수의 개수
def era_factor_count(N):
    A = [0 for _ in range(N+1)]
    for i in range(1, N):
        for j in range(i, N, i):
             A[j] += 1
    return A

# 활용 2 : 소인수의 합
def era_factor_sun(N):
    A = [0 for _ in range(N+1)]
    for i in range(2, N):
        for j in range(i, N, i):
            A[j] += i
    return A

# 활용 3 : 소인수분해 하기
def era_factorization(N):
    A = [0 for _ in range(N+1)]
    for i in range(2, N):
        if A[i]: continue
        for j in range(i, N, i):
            A[j] = i
    return A

A = era_factorization(100)
N = 84
while A[N] != 0:
    print(A[N])
    N //= A[N]
```

- 빠른 거듭제곱과 모듈러
    - python은 크게 고민하지 않아도 된다.
    - 이런 거듭제곱을 순수핟게 반복문으로 진행하는 것이 아니라 효율적인 방법을 살펴보자.
    

```python
# C/C++ style
def pow_advanced(a, b, mod):
    ret = 1
    while b > 0:
        if b % 2: ret = ret*a%mod
        a, b = a*a%mod, b//2
    return ret

    print(pow_advanced(3, 1000000, 10000007))
    print(pow(3, 1000000, 10000007))
    print(3**1000000%10000007)
```
