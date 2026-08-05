# 내장함수(built-in function)
'''
- 파이썬이 미리 만들어 내장되어 있는 함수
- import 문을 사용하지 않고 사용하는 함수

form typeHint import add
add()
https://docs.python.org/ko/3/library/functions.html
'''

# 수치 관련 내장 함수들
# abs() :절댓값 반환

print(abs(-10))

# min(), max(), sum()
print(min([1, -5, -10]))
print(max([1, -5, -10]))
print(sum([1, -5, -10]))

# pow(x,y), divmod(a,b)
print(pow(10,3))
print(divmod(10,3))

# round(): 실수를 반올림, int() 소수점 제거
# 참고. math 모듈의   floor(),       ceil() 함수
#                   floor() : 내림, ceil() 올림

print(round(3.1415,3))
print(int(3.55555))
import math

print(math.ceil(3.1415123))
print(math.floor(3.1415123))

from math import ceil, floor

print(ceil(3.1415123))
print(floor(3.1415123))

# 문자코드 관련 함수 : chr(), ord(), ascii()
'''
chr(정수) : 유니코드 값을 문자로 반환
ord(문자) : 문자를 유니코드 값으로 변환
ascii(객체) : 객체를 ASCII 문자열로 표현
'''

print(chr(48))
print(chr(97))
print(chr(8316))
print(chr(44032))
print(chr(44034))

print(ord('A'))
print(ord('가'))
# print(ord('가오가이거'))

print(ascii('python'))
print(ascii('가나다'))
print(ascii(['가', '|uac00']))

'''
any() : 하나만 True 여도 True
all() : 모두 True인 경우만 True

'''
print(any([True, False, False]))
print(all([True, False, False]))
print(any([True, True, True]))

print(any([0,0,5]))
print(all([0,0,5]))
print(all([1,2,5]))
print(all([-1,2,5]))

# 정수 진법변환 : bin(), oct(), hex()
# 문자열을 숫자로 변환 : int(), float(),
# 숫자를 문자열로 변환 : str(),
# 논리형으로 변환 : bool(),
# 데이터 유형 반환 : type(),
# 객체의 주소값(레퍼런스) 반환 : id()
# 출력/입력 : print(), input(),
# 자료구조 생성/변환 : list(), tuple(), dict(), set(),
# 표현식 그대로 연산 수행/실행 : eval(),
print(eval('10'))
print(eval('10.5'))
print(eval('10.5 + 33'))


# 지정하는 범위값을 반복가능한 객체로 반환 : range(start, stop, step)
# 요소의 길이 반환 : len()
# 객체 메모리 제거 : del()
# 요소 정렬 : sorted()
# 요소 역순으로 : reversed()

# map(function, iterable) : iterable 각 요소가 함수 function에 의해 수행된 결과 반환
def plus10(x):
    return x+10

print(list(map(plus10, [1,2,3,4])))
print(tuple(map(plus10, (1,2,3,4))))
print(tuple(map(lambda x:x+10, (1,2,3,4))))

# filter(function, iterable) :
#   반복가능한 자료형의 요소들이 함수 function에 입력되었을 때 True인 결과만 묶어서 반환

def positive(x):
    return x>0

print(list(filter(positive, [-10, 3,4,0,-7,5])))
print(list(filter(lambda x:x%2==1 and x>=0, [-10, 3,4,0,-7,5])))

# zip(*iterable) : 각 iterable에서 동일한 인덱스의 요소를 추출하여 묶어서 반환
print( list( zip([1,2,3], ['one', 'two', 'three']) ) )
print( list( zip([1,2,3,10], ['one', 'two', 'three']) ) )
print( list( zip([1,2,3], ['one', 'two', 'three', 'ten']) ) )
# print( list( zip([1,2,3], ['one', 'two', 'three', 'ten']), strict=True ) )
# TypeError: list() takes no keyword argument

# enumerate() : 인덱스 값을 포함하는 enumerate 객체 반환
print(list(enumerate(['피자', '치킨', '떡볶이'])))
print(list(enumerate(['피자', '치킨', '떡볶이']))[1])




















