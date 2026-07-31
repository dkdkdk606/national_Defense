# 리스트 요소 삭제(제거)

# 리스트.remove(값) 먼저 찾아지는 값 1개 제거

fruits = ['apple', 'banana', 'coconut', 'melon', 'kiwi', 'mango']
fruits.remove('apple')
print(fruits)

fruits = ['apple', 'banana', 'coconut', 'melon', 'kiwi', 'mango', 'apple', 'kiwi', 'mango']
fruits.remove('apple')
print(fruits)

# 모든 'apple' 삭제하기
fruits = ['apple', 'banana', 'coconut', 'melon', 'kiwi', 'mango', 'apple', 'kiwi', 'mango']
print(fruits)
n = fruits.count('apple')
for i in range(n):
    fruits.remove('apple')
    print(fruits)

# 리스트.pop() -> 마지막 요소를 반환하고 리스트에서 제거
print(fruits.pop())
print(fruits)

fruits = ['apple', 'banana', 'coconut', 'melon', 'kiwi', 'mango', 'apple', 'apple', 'kiwi', 'mango']
for i in range(len(fruits)):
    fruits.pop()
    print(fruits)

# 리스트.pop(인덱스) => 인덱스의 요소를 반환하고 리스트에서 제거
fruits = ['apple', 'banana', 'coconut', 1, 'kiwi', 'mango', 'apple', 'apple', 'kiwi', 'mango']
print(type(fruits.pop(3)))
print(fruits)

# 리스트 확장: 리스트.extend(리스트)
#   - 이전 리스트 요소들을 추가하여 확장된 리스트 반환

fruits = ['apple', 'banana', 'coconut', 'melon', 'kiwi']
fruits.extend(['kakao', 'berry'])
print(fruits)