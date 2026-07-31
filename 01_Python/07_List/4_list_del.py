# 리스트 삭제

names = ['김', '이', '홍', '박', '최', '성']
print(names)

# del(리스트요소) 함수를 사용
del(names[1])
print(names)

del(names[3:])
print(names)

# del(names[:])
# print(names)
print('*'*30)
names = ['김', '이', '홍', '박', '최', '성']
print(names[1:4])
names[1:4] = []
print(names)

# 리스트 자체 삭제
# 1) del() 함수 사용    : 메모리에서 제거
a = [10, 20, 30]
print(a)
del(a)
# print(a) # 메모리에서 완전 사라져서 변수 호출 자체가 안됨

# 2) None을 대입        : None 유형으로 변경
b = [10, 20, 30]
b = None 
print(b)

# 3) []을 대입          : 빈리스트로 변경
c = [10, 20, 30]
c = []
print(c)








