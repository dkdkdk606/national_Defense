# 튜플 관련 메서드

t = 'a', 'a', 'a', 'b', 'c', 'd', 
print(t)

# list1 = ['a', 'a', 'a', 'b', 'c', 'd', ]

# 요소의 위치
print(t.index('a'))
print(t.index('b'))
print(t.index('a', 2))
print(t.index('a', 1, 3)) # 1~3 인덱스 범위에서 b의 위치를 찾음
print(t.index('b', 3, ))  # 찾는 요소가 없는 경우 오류 발생

print('-'*30)
# 일치하는 요소의 수 : count()
print(t.count('a'))
print(t.count('e'))

