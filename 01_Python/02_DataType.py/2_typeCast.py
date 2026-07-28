# 자료 형변환

# 형변환 함수
'''
    - int(문자열) : 문자열을 정수로 변환
    - float(문자열) : 문자열을 실수로 변환
    - str(정수 또는 실수) : 숫자를 문자열로 변환
'''

age = 30
name = '홍길동'
weight = 75.5
print(f'{name}의 나이는 {age}입니다.')
# print(name + '의 나이는 ' + age + '입니다.')
print(name + '의 나이는 ' + str(age) + '입니다.' + '몸무게는 ' + str(weight) + '입니다.' )

age = '30'
weight = '75.5'
# print( name + '의 20년 뒤 나이는? ', age + 20)
print( name + '의 20년 뒤 나이는? ', int(age) + 20)
# print(f'{name}은 체중이 10kg 감량되어 현재 {weight - 10}kg 이다')
print(f'{name}은 체중이 10kg 감량되어 현재 {float(weight) - 10}kg 이다')

# int(문자열, base=진수)
number = 'ff'
print(f'{number}를 16진수로 읽어 10진수로 표현 {int(number, base=16)}')
number = '123'
print(f'{number}를 8진수로 읽어 10진수로 표현, {int(number, base=8)}')

