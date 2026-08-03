# 딕셔너리(dictionary)
'''
- 리스트와 같이 자주 사용되는 데이터 구조
- 데이터 분석, AI, 웹, API개발 등의 실무에 많이 활용되는 구조
- 집합적 자료형
- 데이터 저장 순서가 없음
- 키로만 값에 접근 가능

- 키(key)와 값(value)의 쌍으로 이루어진 구조
    - 형식 : { 키1:값1, 키2:값2, ...}
    - 중괄호{} 로 묶어 구성
    - 키 : 중복 불가, 변경 불가한 데이터를 사용(정수, 실수, 문자열, 튜플)
    - 값 : 어떤 데이터든 다 가능(정수, 실수, 논리, 문자열, 리트, 튜플 등)
    - key:value 한 쌍을 item이라고 부름
    - item 은 쉼표(,)로 구분
    - 다른 프로그래밍 언어에서는 해시(hash), 연관배열(associative array)이라 부름

- 키 값으로 접근(인덱스 접근 불가)
    
'''

# 딕셔너리 생성
#  방법1. {} 사용

std = { 'name':'홍길동', 'age':20, 'addr':'seoul'}
print(std, type(std))

# 방법2. dict()함수 사용
d = dict()
print(d, type(d))

# 딕셔너리 접근
'''
- key를 통해서만 접근
'''

print(std['addr'])

# 딕셔너리 요소 추가
std['tel'] = '010-0000-1111'
print(std)

d[1] = 'a'
d[3] = 'tel'
print(d)

d[4] = 10
d[1] = 100
print(d)

# 키는 유일한 값(unique)
# 동일한 키를 갖는 값을 추가할 경우 마지막에 입력한 값만 적용

d[5] = d
print(d[5])

# 딕셔너리 요소 삭제
#   : del() 사용

d = {'one':1, 'two':2, 'three':3}

d['four'] = 4
print(d)

del(d['four'])
print(d)

del(d)      # 딕셔너리 변수 자체를 제거
# print(d) 
