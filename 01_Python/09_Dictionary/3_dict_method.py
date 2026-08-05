# 딕셔너리 관련 주요 메슫
'''
- keys() : 키값 뱉음
- values () : 값 뱉음
- items() : 키:값 쌍으로 뱉음
- get(키[, x]) : 지정한 키의 값을 반환 (키가 없으면)
# 키[, x] 키가 들어가거나 안들어가도 된다 -> 오류 반환 안함
- setdefualt(키[, x]) : get() 메서드와 같은 열할, 키에 해당하는 값이 없으면 그 값을 설정
- copy() : 딕셔너리 내용을 새로운 딕셔너리에 복사
            새 딕셔너리 = 딕셔너리.copy()
- update() : 딕셔너리2의 모든 항복을 딕셔너리1에 갱신
            딕셔너리1.update(딕셔너리2)
- pop(키) : 키 항목의 값을 반환하고 딕셔너리에서 제거
- poptime() : 키 항목의 (키, 값)을 반환하고 딕셔너리에서 제거
- clear() : 딕셔너리의 모든 항목을 삭제

'''

# get(키[, x]) : 지정한 키의 값을 반환 (키가 없으면)

d = {'one':1, 'two':2, 'three':3}
print(d)

value = d['two']
print(d)
value = d.get('two')
print(d.get('two'))
print(d)
print(value)

# []를 사용하여 딕셔너리의 키를 접근할 때 해당 키가 없으면 오류 발생
# value = d['four']  # KeyError: 'four'
# print(d)
value = d.get('four')
value = d.get('four', 4)
# get을 사용하여 키를 접근할 때 키가 없으면 None 반환
print(d.get('four'))
print(d)
print(value)

print('-'*30)

# - setdefualt(키[, x]) : get() 메서드와 같은 열할, 키에 해당하는 값이 없으면 그 값을 설정
# 키 값이 없는 경우 지정한 키값을 갖는 요소를 추가
value = d.setdefault('four')
print(value)
print(d)    

value = d.setdefault('five', 5)
print(value)
print(d)

print('-'*30)
# - copy() : 딕셔너리 내용을 새로운 딕셔너리에 복사(깊은복사)
#             새 딕셔너리 = 딕셔너리.copy()
d2 = d.copy()
print(d)
print(d2)

d['six'] = 6
print(d)
print(d2)

# - update() : 딕셔너리2의 모든 항복을 딕셔너리1에 갱신
#             딕셔너리1.update(딕셔너리2)

print('d => ', d)
d3 = {'nine':9, 'ten':10}

d.update(d3) # d + d3
print(d)
print(d3)
print('-'*30)
d.update({'two':20, 'nine':None})
print('d => ', d)

# - pop(키) : 키 항목의 값을 반환하고 딕셔너리에서 제거
value = d.pop('nine')
# del(d['nine'])
print(value)
print('d => ', d)

# - poptime() : 키 항목의 (키, 값)을 반환하고 딕셔너리에서 제거
print(d.popitem())

#  키 값 튜플 항목을 반환하고 딕셔너리에 추가
key, value = d.popitem()
print(key, value)
print('d => ', d)
key, value = d.popitem()
print(key, value)
print('d => ', d)
key, value = d.popitem()
print(key, value)
print('d => ', d)

#clear 메로리에서 딕셔너리 객제 제러
d.clear()
print(d)

# del(d)    # 메모리에서 딕셔너리 객체 제거

# 문제, 다음의 딕셔너리를 이용하여 학생 성적 출력하기
students = {'Lee':97, 'Choi':85, 'Bang':100}

#1 모든 학생 출력
for key in students.keys():
    print(students[key])

#2. 평균 점수 계산
print(f'{sum(students.values())/len(students)}')
total = 0
for i in students.values():
    total += i
print(f'{total / len(students):.1f}')

#3. 최고 점수 학생 이름 출력

high_score = 0
student = ""
for key in students.keys():
    if high_score < students[key]:
        high_score = students[key]
        student = key
print(student)

# scores = list(students.values())
# max_value = scores[0]
# for i in range(1, len(scores)):
#     if max_value < scores[i]:
#         max_value = scores[i]




# high_score = 0
# student = ""
# for name, score in students.items():
#     if high_score < score:
#         high_score = score
#         student = name
# print(student)

# student = max(students, key=students.get)
# print(student)

# scores = list(students.values())
# scores.sort()
# for name, score in students.items():
#    if score == scores[-1]:
#        print(name, "00000000000000000000")

# r_d = {score:name for name, score in students.items() }
# print(max(r_d))
# print(r_d.get(max(r_d)))


#4 'bang' 학생의 점수를 90으로 수정
students['Bang'] = 90

#5 'Lee' 학생 삭제
del(students['Bang'])

print(students)

for i in range(len(students)):
    name, score = students.popitem()
    print(f'{i+1}: {name}, {score}')
print(students)


