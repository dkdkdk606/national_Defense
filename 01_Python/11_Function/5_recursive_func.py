# 재귀함수(recursive function)
'''
- 자신을 함수 내부에서 호출하는 함수


'''

def self_call():
    print('하', end='')
    self_call()

# self_call()
# 함수 내부에 자신을 되부르는 호출 시 무한 호출이 발생하면서 스택오버플로우(stack overflow) 발생
# 반드시 무한호출이 되지 않도록 호출이 반환되는(중단되는) 코드를 넣어주어야 함

def self_call2(n):
    if n==0:
        return 0
    else:
        print('하', end='')
        self_call2(n-1)

self_call2(50)

print()
# 문제1. 정수 a부터 b 까지 더하는 함수 (a <= b)
def add_ab(a, b):
    result = sum(range(a, b+1))
    return result

print(add_ab(6, 10))

# 문제2. 정수 a부터 b 까지 더하는 재귀함수 (a <= b)
def add_recur(a, b, total = 0):
    total += a
    if a == b:
        return total
    else:
        a += 1
        return add_recur(a, b, total)

def add_recur0(a, b):
    if a == b:
        return a 
    else:
        return a + add_recur(a+1, b)

print(add_recur0(6, 10))

def add_recur2(n):
    if n==1:
        return 1
    return n + add_recur2(n-1)

n = 10
print(f'1부터 {n}까지의 합은 {add_recur2(n)}')

# 문제3. n 번째 피보나치 수열 생성하는 함수
#   => 메모리 낭비 가져오는 재귀 구조 -> 1번 루프 돌 떄 마다 메모리 거의 2배로 먹음

def fibo(n):
    if n-1 <= 0: 
        return 0
    elif n-1 == 1:
        return 1
    a, b = 0, 1
    return fibo(n-2) + fibo(n-1)

print(fibo(7))



