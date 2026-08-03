# 튜플(tuple)
'''
 - 리스트와 유사한 시퀀스 자료형
 - 추가/수정/삭제 불가
 - 읽기 전용 자료로 사용하기 위해
 - 튜플의 생성 : () 또는 tuple() 함수를 사용
 - 튜플의 요소들은 인덱스([])로 구분 
'''

# 튜플 생성
t1 = (1, 2, 3)
t2 = 4, 5, 6
t3 = t1, 6, 7, 8
t4 = [1, 2], [3, 4]
t5 = tuple([5, 6, 7, 8])    #리스트를 튜플로 변환
t6 = tuple('python')        # 문자열의 문자들을 튜플로 변환
t7 = tuple()

print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))
print(t4, type(t4))
print(t5, type(t5))
print(t6, type(t6))
print(t7, type(t7))

print('-'*30)
# 튜플의 특징
t = 1, 2, 3
# 1)인덱싱 : []기호를 사용하여 튜플의 요소 접근
print(f't[0] => {t[0]}')

# 튜플의 요소를 할당문을 이용하여 변경 불가
# t[0] = 10
# TypeError: 'tuple' object does not support item assignment

# 튜플 요소 추가 불가
# t.append(4) # append() 와 같이 튜플의 요소를 추가하는 메소드는 없음

# 튜플의 요소 삭제
# del(t[0]) # TypeError: 'tuple' object doesn't support item deletion
# del() 함수를 이용하여 튜플의 요소를 삭제할 수 없음

# 튜플 객체는 삭제 가능
del(t)