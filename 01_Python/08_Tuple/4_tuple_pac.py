# 튜플의 팩킹(Packing)과 언팩킹(Unpacking)

'''
- 패킹(Packing): 한 데이터에 여러 개의 데이터를 넣는 것
- 언팩킹(Unpacking): 한 데이터에서 데이터를 각각 꺼내오는 것
'''

# 패킹
t = 1, 3.14, 'hello'
print(t, type(t))

# 언팩킹
x, y, z = t         
print(x, y, z)

# x, y, z = 1, 2, 3

# 확장된 언패킹
t = 1, 2, 3, 4, 5
# a, b, c = t      # 오류 발생
a, b, *c = t   
# ValueError: too many values to unpack (expected 3, got 5)
print(a)
print(b)

*a, b = t
print(a, b, c)
a, *b = t
print(a, b, c)

*a, b, c = t
print(a, b, c)

# a, *b, *c = t # 2개 쓰는건 불가
# print(a, b, c)


