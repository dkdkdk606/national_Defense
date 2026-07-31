# 리스트 복사

names = ['김', '이', '홍', '박', '최', '성']
a = 10
b = a
print(a, b, id(a), id(b))
a = 20
print(a, b, id(a), id(b))

new_names = names
print(names, id(names))
print(new_names, id(new_names))

names[1] = '선우'
print(names, id(names))
print(new_names, id(new_names))

# 깊은 복사(deep copy
new_names2 = list(names)
print(names, id(names))
print(new_names2, id(new_names2))


names[-1] = '허허'
print(names, id(names))
print(new_names2, id(new_names2))