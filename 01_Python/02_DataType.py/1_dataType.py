# 자료형(data type)
# 컴퓨터로 표현할 수 있는 데이터의 종류

# 파이썬의 자료형
#  - 고수준의 자료형으로 다양한 정보를 저장할 수 있는 자료형 제공
#  - 주요 내장 자료형(built-in type)
'''
    - bool : True, False 로 나타내는 자료형(논리)
    - int : 정수    ex) 123
    - float : 실수  ex) 12.3    1e-5    1.234e4
    - complex : 복소수  ex) 5+3i
    - str : 문자열  ex) 'hi', 'banana', ''' ''', """ """
    - bytes : 0~255 사이의 코드 모임    ex) b'python'
    - list : 순서가 있는 파이썬 객체 집합   ex) [1, 2, 3]
    - dict : 순서가 없는 파이썬 객체 집합   ex) {'name':'hong', 'addr':'seoul'}
    - tuple : 순서가 있는 파이썬 객체 집합, 내용 변경 불가  ex) (1, 2, 3)
    - set : 집합 표현(중복 허용 불가)   ex) {1, 2, 3}
'''
# dict 순서없음 -> 일반적으로 데이터를 다루게 되면 dict를 쓰게됨
# tuple 은 수정 불가라 고정값 쓸 때
# set 는 집합인데 파이썬에서는 중복되지 않는 값을 원소로 가져 키값으로 많이 씀

print(b'python')
print('python')

# 변수의 자료형
'''
    - 파이썬의 변수는 지정된 자료형이 없음 (가변 자료형)
    - 저장한 값에 따라서 변수의 자료형이 결정됨 (동적 타이핑)
    - 변수값의 주소를 저장하는 레퍼런스
'''
a = 100
print(type(a))
a = 'hello'
print(type(a))

# 정수의 진법 변환
'''
    - bin() : 2진수로 변환
    - oct() : 8진수로 변환
    - hex() : 16진수로 변환
'''

print('2진수로 변환')
print(bin(11), bin(0o11), bin(0x11))
print('8진수로 변환')
print(oct(11), oct(0o11), oct(0x11))
print('16진수로 변환')
print(hex(11), hex(0o11), hex(0x11))


print(bin(0b11))
print(bin(11))
print(oct(11))

