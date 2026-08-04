# 함수의 입력값 : 매개변수(parameter)
'''
    - 파라미터 : 함수에 전달되는 값을 받는 변수
                함수 정의시 사용되는 입력값
    - 인수(argument) : 함수에 실제로 전달되는 값
                함수 호출 시 사용되는 입력값
    - 매개변수의 자료형 : 파이썬의 자료형 모두 사용 가능
    - 매개변수의 수는 0개 이상 사용
    - 매개변수의 요소 숫자가 가변적인 경우 *매개변수명 사용 (가변길이 매개변수)
    - 매개변수의 순서 : 함수 정의시 순서와 실인수 입력 순서가 동일
            => 위치인수(position arguments)
                - 함수 호출 시 위치에 의해 구별하는 방식
                - 매개변수의 순서대로 인수를 전달
    - 매개변수의 기본값을 설정할 수 있다 => 디폴트 매개변수

    - 키워드 인수(keyword argument) : 매개변수 이름 = 값
        - 인수들 앞에 키워드(매개변수)를 두어서 인수를 구별
        - 인수의 위치가 매개변수의 위치와 달라도 됨

'''

def add( a, b ):
    print((f'{a} + {b} = {a+b}'))


add(10, 30)     # 10, 30 : argument

# 문제1. 세 개의 값의 평균을 반환하는 함수

def get_average(x,y,z):
    '''
        x, y, z : 입력 매개변수
    '''
    return f'{(x+y+x)/3:.1f}'

kor = 100
eng = 80
math = 85
value = get_average(kor, eng, math) # kor, eng, math : 인수
print(value)
value = get_average(100, 80, 85) # 인수를 레터럴로 입력
print(f'평균 = {value}')

# 문제2. 두 값의 합을 구하는 함수
def add2(a, b):
    return a+b

# 문제3. 세 값의 합을 구하는 함수
def add3(a, b, c):
    return a+b+c

# 문제 4 네개 값의 합을 구하는 함수
def add4(a, b, c, d):
    return a+b+c+d

# 가변길이 매개변수
#   입력 매개변수의 길이가 가변적인 경우 *를 사용
#   사용형식 : *매개변수명(보통 args로 씀)
#               *args, **args
#   - 가변길이 매개변수 => *args : 튜플 형식, **args : 딕셔너리 형식

def add(*a):
    total = 0
    print(sum(a))
    for i in a:
        total += i
    return total

print('가변길이 매개변수 : *args')
print(add2(1,2))
# print(add3(1,3))  # TypeError: add3() missing 1 required positional argument: 'c'
print(add3(1,2,3))
print(add4(1,2,3,4))
print(add(1,2,3,4,5,6,7,8,9))

print('가변길이 매개변수 : **args')

def info(**kwargs):
    print(kwargs, type(kwargs))
    for k, v in kwargs.items():
        print(k,v)
    

info(id = '123', name='hong')
info(id = '456', name='lee', age = 30)
print('-'*30)




# 디폴트(default) 매개변수
'''
    - 매개변수의 기본값 설정

'''
# 디폴트 매개변수는 기본값이 없는 매개변수 앞에 올 수 없다
# def greeting(name='홍길동', msg): #SyntaxError: parameter without a default follows parameter with a default
    # pass
# 디폴트 매개변수는 뒤에 있어야함

                   # 키워드인수
def greeting(name, msg="hello"):
    print(f'{name}, {msg}!')

greeting("홍길동", "안녕")
greeting("홍길동", "반가워")
greeting("홍길동", "잘 지내지")
greeting("홍길동", )
greeting("홍길동")

def show_info(name, year = 4 , age=23):
    print(name, year, age)

show_info('홍길동')
show_info('성춘향', )
show_info('성춘향', 1)
# show_info('성춘향', ,1) # SyntaxError: invalid syntax
show_info('성춘향', age = 18)
show_info('방자', 4, 30)
# 키워드 인수 뒤에도 키워드 인수만 와야함
# show_info('방자', year = 2, 30) #SyntaxError: positional argument follows keyword argument
show_info('방자', year = 2)

show_info('방자', year = 2, age = 30)

# 위치인수
def sub(a, b):
    return a-b
print(sub(10,5)) # 10 0->a, 5->b

# 키워드 인수 : 인수의 위치가 달라도 됨
print(sub(b=10, a=5))       # b -> 10, a -> 5  

# 위치인수와 키워드 인수를 동시에 사용할 수 있으나
# 위치인수를 키워드 인수보다 앞에 두어야 한다.(디폴트 매개변수)




