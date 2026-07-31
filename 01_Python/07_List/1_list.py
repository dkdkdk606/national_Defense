#  list (리스트)

'''
- 여러 개 값의 모임
- 순서를 가짐 => 시퀀스형 데이터
- 서로 다른 데이터유형을 가질 수 있음
- 동일한 이름을 갖는 원소들의 연속 저장 영역
- 여러 개의 데이터가 저장되어 있는 장소 => 집합적 자료형
- 각 원소는 인덱스(index)로 구분하고, 인덱스로 접근(인덱스는 0부터 시작)
- 값 변경 가능(mutable)
- 리스트는 [](대괄호)
'''

score = 90
kor1 = 90
kor2 = 70

#  리스트 생성
kor = [90, 70, 60, 100]
print(kor, type(kor))

# 리스트의 크기는 가변적
emptylist = []
numList = [20, 10, 30]
strList = ['python', 'C', 'C#']

# 다양한 종류를 한 리스트에 저장 가능
myList = [10, 'dog', 3.14, True]

# 리스트 안에 리스트를 포함
numList = [1, 2, 3, [10,20,50]]

# 리스트의 필요성
# 많은 데이터를 값 하나 저장하는 여러 개 변수를 사용하는 것 보다는 리스트에 한번에 저장 가능
# 예. 4개의 정수를 입력받아 합계 출력: 4개 정수를 다음에도 사용하기 위해 저장
# 

total = 0
num1 = int(input('숫자: '))
total += num1
num2= int(input('숫자: '))
total += num2
num3 = int(input('숫자: '))
total += num3
num4 = int(input('숫자: '))
total += num4
print(total)

print(num1 + num2 + num3 + num4)

scores = []
for i in range(4):
    num = int(input('숫자: '))
    scores.append(num)
print(scores)


a, b, c, d = 10, 20, 40, 50
aList = [10, 20, 40, 50]
print(aList[2])

total = 0
for s in scores:
    total += s  
print(total)

total = 0
for i in range(len(scores)):
    total += scores[i]
print(total)

# 리스트는 반복문을 사용하여 요소를 접근하여
# 변경하거나, 요소를 활용한 다른 작업을 수행하는 경우가 일반적


# 문제. 리스트와 반복문을 사용하여 10개의 정수를 입력받고 합계와 평균계산

scores = []
# total=0
for i in range(10):
    num = int(input('숫자: '))
    scores.append(num)
    # total += i
print(scores)

total = 0
for i in scores:
    total += scores[i]
print(f'{total} {total/10:.1f}')

