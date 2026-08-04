# 함수의 반환
'''
- 반환값(return value) : 함수가 특정 기능을 수행하고 돌려주는 결과 값
- return 문 사용
- return문 사용하지 않은 경우 함수는 반환값이 None
- 함수의 반환값 데이터 형식은 모든 데이터 자료형 가능
    : 숫자, 논리, 문자, 문자열, 리스트, 튜플, 딕셔너리 등
- 함수의 반환값은 변수로 받아서 사용
    변수 = 함수명()
'''

def add():
    num1 = int(input('숫자 1 입력: '))
    num2 = int(input('숫자 2 입력: '))
    return num1 + num2

result = add()

# return문이 여러 개 있으면 첫번째 return 문만 수행
# return문은 하나만 사용할 것
def mulit_return():
    return 1
    return 2
    return 3 # 첫번째 return인 1만 적용됨

print(mulit_return()) # 1

# return하는 데이터 유형1. 숫자
def return_int():
    return 10
result = return_int()
print(result, type(result))


def return_float():
    return 3.14
result = return_float()
print(result, type(result))


def return_str():
    return "ㅎㅎ"
def return_bool():
    return True
def return_tuple():
    return 1,2,3
def return_list():
    return [1, 2, 3]
def return_dict():
    value = {1:'lee', 2:'kang', 3:'choi'} 
    return value

result = return_str()
print(result, type(result))
result = return_bool()
print(result, type(result))
result = return_tuple()
print(result, type(result))
result = return_list()
print(result, type(result))
result = return_dict()
print(result, type(result))

# 문제 1. 가로길이와 세로길이를 키보드로 입력받아 면적과 둘레길이를 구하여 반환하는 함수
#       정의하고 호출하기
'''
함수 이름 get_rectangle()
함수호출 결과
    가로길이 입력 : 10
    세로길이 입력 : 20
    사각형의 면적 : 200
    사각형의 둘레 : 60
'''

def get_rectangle():
    h = float(input("가로길이 입력 : "))
    v = float(input("세로길이 입력 : "))
    return v, h
    # return f'사각형의 면적 : {h*v:.1f} \n사각형의 둘레 : {(h+v)*2:.1f}'
v, h = get_rectangle() 
print(f'사각형의 면적 : {h*v:.1f} \n사각형의 둘레 : {(h+v)*2:.1f}')

# 문제2. 상품가격, 주문수량을 입력 받아 주문액을 계산하여 반환하는 함수 정의 및 호출
'''
함수이름 order()
결과
    상품가격 입력 : 1000
    주문수량 입력 : 5
    --------------------
    상품가격 : 1000원
    주문수량 : 5개
    주문액 : 5000원
'''

def order():
    price = int(input("상품가격 입력 : "))
    quantity = int(input("주문수량 입력 : "))
    print('-'*20)
    print(f'상품가격 : {price}원')
    print(f'주문수량 : {quantity}개')
    print(f'주문액 : {price*quantity}원')

order()



