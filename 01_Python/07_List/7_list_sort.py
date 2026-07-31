# 리스트 정렬
#   - 리스트.sort()     : 자료의 값 기준으로 정렬(원본 변경)
#   - 리스트.reverse()  : 역순
#   - sorted(리스트)    : 자료의 값 기준으로 정렬 (원본은 그대로 유지)


fruits = ['apple', 'banana', 'melon', 'kiwi', 'mango']
print(fruits)
fruits.sort() # 오름차순 a -> z
print(fruits)
fruits.sort(reverse=True) # 내림차순 z -> a

print(fruits)

scores = [90, 70, 81, 64, 89]
scores.sort(reverse=True)
print(scores)

fruits = ['apple', 'banana', 'melon', 'kiwi', 'mango']
new_f = sorted(fruits)
print(fruits)
print(new_f)

charList = ['b', 'A', 'c', 'D', 'E']
charList.sort()
print(charList)

charList = ['b', 'A', 'c', 'D', 'E']
charList.sort(key=str.lower)
print(charList)

charList = ['b', 'A', 'c', 'D', 'E']
charList.reverse()
print(charList)

