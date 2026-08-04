# 람다함수(lambda function)
'''
실무에서 많이 사용되는 함수 중 하나
- 익명의 함수(이름없는 함수)로 한줄로 작성되는 함수
- 일회성으로 사용하는 작은 함수를 만들 때 편리함
- return 문을 사용하지 않음
- 람다함수의 몸체(body)는 문장이 아닌 하나의 식이다

- 람다 표현식 : lambda <인수들> : 반환할 식
                변수명 = lambda 인수들 : 반환할 식

- 람다 함수는 함수 참조를 반환
- 변수로 람다 함수객체를 받아서 람수 호출을 할 수 있다.
'''

def add(a, b):
    return a+b

result = lambda a,b: a+b

# def square(x):
#     return x*x

# 람다함수 정의(람다표 현식)
square = lambda x: x*x
# 람다함수 호출
print(square(10))

# 람다함수 매개변수(인수)에 기본값을 설정할 수 있음
hap = lambda x, y=10: x+y
print(hap(100,30))
print(hap(100))
print(hap(y=10, x=100))

# 람다 표현식을 변수에 할당하지 않고 그 자체를 호출
print((lambda x=10, y=10: x+y)())
print((lambda x=10, y=10: x+y)(1000))
print((lambda x=10, y=10: x+y)(20,40))

# 람다 표현식 밖에 있는 변수 사용 가능
y = 200
print( (lambda x: x+y)(100) )


# 람다 함수 사용 목적
#   : 함수의 인수 부분에서 간단하게 함수를 생성하여 사용하기 위해서
'''
    - 코드 간결화
    - 일회성 함수
    - 함수형 프로그래밍에 사용하는 함수들과 결합 : map(), filter(), sorted()
    - 가독성 개선 : 의미없는 함수 선언 제거
'''

def plus_10(x):
    return x+10
print(plus_10(10))

print(list(map(plus_10, [1, 2, 3])))

print(list(map(lambda x:x+10, [1, 2, 3])))

# 문제. 정수리스트에서 짝수만 추출하여 새로운 리스트 생성하는 함수 정의
#   - 정수리스트를 인수로 줌
#   - 일반적인 함수 형태, 람하 함수 형태 2가지 방법으로 정의

num_list = list(range(10))

def onlyeven(list):
    even_list = []
    for i in list:
        if i % 2 ==0:
            even_list.append(i)
    return even_list

print(onlyeven(num_list))

print('-'*30)
# 람다버전
num_list = list(range(10))
even_list = []

onlyEven = lambda x:even_list.append(x) if x%2 ==0 else ""

list(map(onlyEven, num_list))

print(even_list)


# 문제2 두 리스트의 동일한 인덱스에 있는 값을 합하여 새로운 리스트를 생성하고 반환하는 함수 정의
# 일반적인 함수와 람다 함수 두 가지 방식으로 정의

list1 = [1,2,3,4]
list2 = [10,20,30,40]


def sum_list(list1, list2):
    list_sum = []
    for i in range(len(list1)):
        list_sum.append(list1[i]+list2[i])
    return list_sum

print(sum_list(list1,list2))
list_sum = []
sumList = lambda x: list_sum.append(list1[x]+list2[x])
list(map(sumList, range(len(list1))))
print(list_sum)







