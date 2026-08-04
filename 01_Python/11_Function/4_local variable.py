# 지역변수와 전역변수
'''
지역번수(local variable)
- 함수 내부에서 정의된 변수 : 매개변수
- 함수 안에서만 사용 가능
- 함수 호출 시 생성되고 함수가 종료되면 소멸되어 사용 불가
- 
'''

def show():
    a = 1       # a : 지역변수
    print(a)

a = 100       # a : 전역변수
show()
print(a)

def show2(a):
    a = a+1
    print(a)

show2(10)
print(a)

'''
# 전역변수
- 함수 회부에서 정의된 변수
- 프로그램 내 모든 곳에서 사용 가능
- 동일한 이름의 변수가 함수 외부와 내부에 존재할 때 서로 다른 변수로 인식(원칙)
- 함수 내부에서 전역변수 앖을 변경 가능 : global키워드 사용

'''

a = 1
def show3():
    c = a+b
    print(a, b, c)

b = 2
def add2():
        a = a+1         #   a, b 지역변수
        c = a+b         #    c전역변수
        print(a , b, c)

# add2

# 전역변수를 함수 내부에서 변경하려면 global키ㅝ드 사용
# 동일한 이름의 지역변수와 지역순위 우선순위가 전역 변수보다 높음

def add2():
    global a
    a = 5
    a = a+1
    c = a+b
    print(a, b, c)

add2()

def sub(x,y):
    global a

    a = 7
    x,y = y, x # x, y 교환
    b = 3
    print("함수내부")
    print(a, b, x, y)

a, b, x, y = 1, 2, 3, 4
sub(x,y)
print("함수 회부")
print(a, b, x, y)

# 리스트 함수에 전달할 경우
#   - 전달된 리스트는 내부변수이지만 mutable한 데이터이므로 함수 내부에서의 변경점이 공유됨
#   - 전달된 리스트를 함수 내부에서만 독립적으로 사용하고 외부의 리스트로 변경하고 싶지 않을 경우
#   - copy() 매서드를 사용하여 깊은 목사를 한 뒤 사용해야 함.

def show_list(my_list):
     print('함수 내부 my_list')
     print(my_list)
     print(f'my_list 주소 {id(my_list)}')

     my_list[-1] = 10000 # -> 얕은복사로 인해 값이 변경됨

def show_list2(my_list):
     new_list = my_list.copy()
     print('함수 내부 my_list')
     print(new_list)
     print(f'my_list 주소 {id(new_list)}')

     my_list[-1] = 10000 # -> 얕은복사로 인해 값이 변경됨

my_list = [1, 2, 3, 4]

show_list(my_list)
print('함수 외부 my_list')
print(my_list)
print(f'my_list 주소 {id(my_list)}')

print('-'*30)

show_list2(my_list)
print('함수 외부 my_list')
print(my_list)
print(f'my_list 주소 {id(my_list)}')

# 딕셔너리를 함수에 전달할 경우
#   - 리스트를 전달하는 경우와 동일함
#   - 함수 인자로 전달된 딕셔너리는 함수 내부에서 변경시 원본을 변경하는 것이 됨
#   - 함수 내부에서 원본을 변경하지 않고 전달받은 딕셔너리를 사용하려면 copy() 메서드를 통해 복사한 뒤 사용

def show_dict(info):
     print('함수내부:', info, id(info))
     info['연락처'] = '010-123-1234'

info = {'이름':'홍길동', '나이':30}
show_dict(info)
print('함수외부:', info, id(info))

# global, nonlocal
#  - 함수 외부, 내부 또는 중첩 함수에서 사용되는 동일한 이름의 변수들에 대한 사용 범위 구분


# nonlocal 변수
'''
 - 함수 내부에서 선언된 함수 : 내부 함수(inner function)의 변수 사용 범위를 local 에서 nonlocal로 지정
 - 중첩 함수 내에서 비지역 변수를 대상으로 사용

'''

# 중첩함수(내부함수)
# def func():
#     #  global a
#      a = 10
#      def inner_func():
#           a = 20
#           print('inner_func():', a)
#      inner_func()
#      print('func():', a)

def func():
     a = 10
     def inner_func():
          nonlocal a
          a = 20
          print('inner_func():', a)
     inner_func()
     print('func():', a)



a = 100
func()
print('전역변수:', a)
     