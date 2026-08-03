# 튜플의 연산

# 1. 요소 접근(인덱싱)

t = "apple", "banana", "berry", 'melon'
print(t)

for i in range(len(t)):
    print(f't[{i}] => {t[i]}')

# 슬라이싱
print(t[1:])
print(t[::2])
print(t[::-1])

# 더하기 연산(+)
t1 = 3, 4, 5
t2 = 10, 11, 1
t3 = t1 + t2
print(t3)

# 반복 : 곱하기 연산(*)
t1 = ('Hi',)
print(t1, type(t1))
print(t1 * 10)

# 튜플의 길이 : len()
print(len(t1*10))

# 튜플의 멤버 확인 : in, not in
t = "apple", "banana", "berry", 'melon'
print('kiwi' in t)
print('apple' in t)
print('kiwi' not in t)