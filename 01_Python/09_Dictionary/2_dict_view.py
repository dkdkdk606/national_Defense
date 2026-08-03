# 딕셔너리 뷰(view)
'''
- 뷰 : 딕셔너리의 요소들을 동적으로 볼 수 있게 하는 객체
- keys() : key에 대한 딕셔너리 뷰 반환
- values() : value에 대한 딕셔너리 뷰 반환
- items() : 항목(key:value)들의 딕셔너리 뷰 반환

'''


d = {'one':1, 'two':2, 'three':3}
print(d)

keys = d.keys()
print(keys, type(keys))

d['four'] = 4
print(d.keys())

# values()
values = d.values()
print(values, type(values))

for key in keys:
    print(key)
for value in values:
    print(value)

# items()
items = d.items()
print(items, type(items))
# print(items[1], type(items[1]))  -> 안됨

for item in items:
    print(item)

# 다음과 같은 자료를 갖는 딕셔너리를 생성하시오.
'''
키          값
-----------------------------
학생        1000
이름        홍길동
학과        컴퓨터학과
성별        남
'''

student = { '학생':1000, '이름':'홍길동', "학과":'컴퓨터학과', '성별':'남'}
# student['학생'] = 1000
# student['이름'] = '홍길동'
# ...

# 생성한 딕셔너리에 연락처가 010-111-1111 추가
student['연락처'] = '010-111-1111'

#'학과 의 값을 AI학과 로 수정
student['학과'] = 'AI학과'

# 키 '학과'를 삭제
del(student['학과'])

print(student)


# 문제 2 키보드로 다음과 같이 한 학생의 정보를 입력하여 학생 딕셔너리를 생성
student1 = {}
keys = ('이름', '나이', '학과') # 따로 키값 지정해주는게 좋긴 하겠네

student1['이름'] = input("이름: ")
student1['나이'] = input("나이: ")
student1['학과'] = input("학과: ")
print(student1)

# student1 = {
#     '이름' : input("이름: "),
#     '나이' : input("나이: "),
#     '학과' : input("학과: "),
# }





student_ex = {}
keys = ('이름', '나이', '학과')
for key in keys:
    student_ex[key] = input(f'{key}: ')
print(student_ex)



# 문제3. 5명 학생 정보를 2번과 같이 입력받아 생성하여 저장

students = {}
for i in range(5):
    students[f'학생{i+1}'] = {}
    students[f'학생{i+1}']['이름'] = input(f'학생{i+1} 이름')
    students[f'학생{i+1}']['나이'] = input(f'학생{i+1} 이름')
    students[f'학생{i+1}']['학과'] = input(f'학생{i+1} 이름')
print(students)


# students = {}
# keys = ('이름', '나이', '학과')

# for i in range(5):
#     students[f'학생{i+1}'] = {}
#     for key in keys:
#         students[f'학생{i+1}'][key] = input(f'학생{i+1} {key}')
# print(students)

# students_ex = []
# student = {}
# for i in range(5):
#     for key in keys:
#         student[key] = input(f'{key}: ')
#     students_ex.append(student)
# print(students_ex)