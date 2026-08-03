# 집합 연산 & 매서드

s1 = {1,2,3}
s2 = {3,6,1}

# print(s1 + s2) : + 연산 불가

# 집합 요소 추가 : add(s), update(s)
'''
- add(element) : add an element to a set
- update(elements) : update the set, adding elements from all others
'''
s1.add(13)
print(s1)

s1.update(s2)
print(s1)

# 집합 요소 삭제 : clear(), discard(), pop(), remove()

s1.clear()
print(s1)

s1 = {1, 2, 3, 6, 13}
print(s1)
# s1.discard() # 삭제하려는 요소가 없는 경우에도 처리
# Unlike set.remove(), the discard() method does not raise an exception when an element is missing from the set.

s1.discard(13)
print(s1)

# s1.remove(16) # 삭제하려는 요소가 없는 경우 KeyError 발생
# #KeyError: 16
print(s1)

# pop() : 집합의 요소 하나를 삭제하며 반환, 비어있는 경우 삭제할 때 오류
print(s1.pop())
print(s1)

# 합집합 : A|B, A.union(B)
print(s1|s2)
print(s1.union(s2))
print(s2|s1)
print(s2.union(s1))


# 교집합 : A&B, A.intersection(B)
print(s1 & s2)
print(s1.intersection(s2))
print(s2 & s1)
print(s2.intersection(s1))


# 차집합 : A-B, A.difference(B)
print(s1 - s2)
print(s1.difference(s2))

print(s2 - s1)
print(s2.difference(s1))


