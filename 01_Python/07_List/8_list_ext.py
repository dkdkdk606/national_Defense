# 리스트 위치 반환 : 리스트.index(값)

fruits = ['melon', 'mango', 'kiwi', 'banana', 'apple']
print(fruits.index('kiwi'))
# print(fruits.index('kakao')) -> 없는값 검색하면 오류

# 리스트 일치 검사 : 비교연산자 사용하여 두 리스트 비교

a = [1, 2, 3, 4]
b = [1, 2, 3]
print(a == b)

print(a >= b)
print(a > b)

# 리스트 조작 함수 : min(), max(), sum() 내장함수
print(min(a), max(a), sum(a))

a = ['c', 'a', 'A', 'z'] # 'A' = 65, 'a' 97
print(min(a), max(a))

# 2이차원 리스트 : 리스트 안에 리스트
b = [[1,2,3], [4,5,6], [7,8,9]]
print(b)
print(b[1])
print(b[1][-1])


b = [[1,2,3], [4,5], [7,8,9,10]]
print(b)
print(b[1])
print(b[1][-1])

kor = [1,2,3]
eng = [4,5,6]
math = [7,8,9]
names = ['Hong', 'Lee', 'Choi']
scores = [names, kor, eng, math]
print(scores)

