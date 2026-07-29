# 산술연산자
'''
    - 이항연산자
        : + : 더하기, - : 빼기, * : 곱하기, / : 나누기
    -     % : 나머지, // : 몫, ** : 제곱
'''

num1 = 10
num2 = 3
print(f'{num1}+{num2}={num1+num2}')
print(f'{num1}-{num2}={num1+num2}')
print(f'{num1}*{num2}={num1*num2}')
print(f'{num1}/{num2}={num1/num2}')
print(f'{num1}/{num2}의 나머지 = {num1%num2}')
print(f'{num1}/{num2}의 몫 = {num1//num2}')
print(f'{num1}의 {num2}거듭제곱 = {num1**num2}')

# 산술연산자 우선순위
'''
    - 동등한 우선순위를 갖는 연산자들은 왼쪽에서 오른쪽으로 가면서 연산 수행
    - +, -  <  *, /, %, //  <  **  <  (~~)
'''
expr = 10 * 3 - 5 ** 2 / 4 % 2
# expr = 10 * 3 -     25 / 4 % 2
# expr =   30   -     25 / 4 % 2
# expr =   30   -      6.25  % 2
# expr =   30   -          0.25
# expr =   29.75
print(f'10 * 3 - 5 ** 2 / 4 % 2 = {expr}')

# 연습문제1. 10000초는 몇분 몇초 인가?
print(f'10000초는 {10000//60}분 {10000%60}초 입니다.')

# 연습문제2. 74350원은 만원, 오천원, 천원, 오백원, 백원, 십원으로 
MONEY = 74350
Money_rest = MONEY
print(f'{MONEY}원은 만원짜리 {Money_rest//10000}장, ', end="")
Money_rest = Money_rest%10000 
print(f'오천원짜리 {Money_rest//5000}장, ', end="")
Money_rest = Money_rest%5000 
print(f'천원짜리 {Money_rest//1000}장, ', end="")
Money_rest = Money_rest%1000 
print(f'오백원짜리 {Money_rest//500}개, ', end="")
Money_rest = Money_rest%500 
print(f'백원짜리 {Money_rest//100}개, ', end="")
Money_rest = Money_rest%100 
print(f'십원짜리 {Money_rest//10}개, ', end="")
print(f'로 지불할 수 있습니다.')

# 대입연산자 : = 과 산순연산자를 함께 사용
'''
    =   : a = 10
    +=  : a += 10   =>  a = a + 10
    -=  : a -= 10   =>  a =  a - 10
    *=  : a *= 10   =>  a =  a * 10
    /=  : a /= 10   =>  a =  a / 10
    **= : a **= 10   =>  a =  a ** 10
    %=  : a %= 10   =>  a =  a % 10
    //= : a //= 10   =>  a =  a // 10
'''