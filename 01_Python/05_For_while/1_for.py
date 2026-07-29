# 반복문(loop)
#   : 조건이 만족하는 경우 반복적으로 문장(들)을 수행
'''
    for 문  : 반복범위가 주어짐
    while문 : 조건이 주어짐
'''

# for 문 형식
'''
    for 변수 in 대상:
        반복문장들 (변수를 사용)
'''
# 1~10사이의 정수를 출력
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i, end=" ")

# range() 함수
'''
    range(stop)     : 0부터 stop-1까지의 정수
    range(start, stop) : start에서 stop-1 까지의 정수
    range(start, stop, step) : start에서 stop-1까지 step씩 커지는 정수
'''

print()

for i in range(1,10):
    print(i, end=" ")

print()

for i in range(10):
    print(i, end=" ")

result = ''
for fruit in ['apple', 'banana', 'mango']:
    result += fruit + ' '
print(result)

for i in range(0,10,3):
    print('반가워요')
    print(i)
    i=10
    print(i)
    # 4번출력

# 반복을 나타내는 변수를 사용하지 않는 경우 위처럼 i 를 쓰는경우 i변수 사용 불가?
for _ in range(0,10,3):
    print('반가워요')



# range(a,b) a=<  <b 정수
# range(a,b,  간격  ) a=<  <b 

# 문제 1. 1~100까지의 합 계산하여 출력하기
sum = 0
for i in range(1,101):
    sum += i
print(f'1부터 100까지의 합 = {sum}')

# 문제 2. 두 정수 사이의 숫자들의 합계 계산하고 출력하기
# 두 정수는 입력받음
a, b = int(input("숫자 1 입력 : ")), int(input("숫자 2 입력 : "))
if a>b:
    max_v = b
    b = a
    a = max_v

sum2 = 0
for i in range(a,b+1):
    sum2 += i
print(f'{a} 부터 {b}까지의 합 : {sum2}')




# 문제 3. 두 정수 사이의 3의 배수들의 합 구하고 출력하기
a, b = int(input("숫자 1 입력 : ")), int(input("숫자 2 입력 : "))
if a>b:
    max_v = b
    b = a
    a = max_v
'''
if a>b:
    max_v = a, min_v = b
else
    max_v = b, min_v = a
'''

sum3 = 0
for i in range( a if a%3==0 else a+(3-a%3) , b-(b%3-1), 3 ):
# for i in range( a + (a%3^3)%3 , b-(b%3-1), 3 ):
    sum3 += i
print(f'{a} 부터 {b}까지 3의 배수들의 합 : {sum3}')

'''
for i in range( a, b+1)
    if i % 3 ==0:
        sum3 += i

'''


# 문제4. 카운트다운
cnt = int(input('시작 숫자를 입력하세요 : '))
for i in range(cnt):
# for i in range(cnt, 0, -1):
    print(i, end=" ")
print('발사')

'''
시작숫자를 입력하세요 : 7
7 6 5 4 3 2 1 발사
'''

# 문제5. 74359원을 지폐와 동전으로 교환하려고 한다. 교환된 지폐와 동전 출력하기
# 지폐 오만원, 만원, 오천원, 천원 / 동전 500원, 100원, 10원, 1원
# 반복문 사용하기

money = 74359
print(f'{money}원은', end=' ')

money_left = money
for i in [50000, 10000, 5000, 1000]:
    print(f'{i}원권 {money_left//i}매', end=' ')
    money_left = money_left % i
#   money_left %= i

print('\\ ')

for i in [500, 100, 10, 1]:
    print(f'{i}원 동전 {money_left//i}개', end=' ')
    money_left = money_left % i