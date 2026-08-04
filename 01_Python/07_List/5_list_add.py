# 요소 추가

# list.append() : 리스트의 맨 뒤에 요소 추가
fruits = ['apple', 'banana', 'melon', 'kiwi']
fruits.append('mango')
print(fruits)
fruits.append(['mango', 'berry'])
print(fruits)

# list.insert(위치, 값) : 특정 위치에 요소를 삽입한다. 마지막에는 삽입 불가
fruits.insert(2, 'coconut')
print(fruits)
fruits.insert(-1, 'coconut')
print(fruits)

# list.extend(위치, 값) : 특정 위치에 요소를 삽입한다.
# 언패킹, 패킹 통해 하나의 리스트로 만듦
