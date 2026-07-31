# 인덱스 요소 접근
# - 인덱싱(indexing)
# - 리스트 인덱스는 0부터, 마지막 요소는 -1로 접근

scores = [90, 80, 100, 70]
for i in range(len(scores)):
    print(i, scores[i])
print()

scores = [90, 80, [100, 70]]
print(scores[2], type(scores[2]))
print(scores[2][0], type(scores[2][0]))
print(scores[-1], scores[-1][-1])

# 리스트 요소 변경
scores[-1] = 1000
print(scores)

scores[-1] = [100, 300, 500]
print(scores)

scores[-1][-1] = 50
print(scores)

# 슬라이싱(slicing)
# - 리스트에서 범위를 지정하여 원하는 요소들을 선택 => 리스트
# - 형식 : 리스트[start:stop]
#   => start에서 stop 까지의 요소를 갖는 리스트 반환
# - 형식 : 리스트[start:stop, step]
#   => start에서 stop 까지 step간격의 요소를 갖는 리스트 반환

print(scores[:])
print(scores[:-1])
print(scores[1:3])
print(scores[1:])
print(scores[::2])
print(scores[::-1])
print('*'*30)

# 리스트 요소 변경
scores = [10, 20, 30, 40]
print(scores)
scores[-1] = 1000
print(scores)
scores[1:2] = [200,300]
print(scores)

scores[1] = [200,300]
print(scores)

# 리스트 더하기: + 연산 => 두 리스트 합치기
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

# 리스트 곱하기: * 연산 => 리스트를 지정한 수 만큼 생성하여 하나의 리스트로 합침
print(a*10)

# 리스트의 길이 : len() 함수 => 리스트의 요소 수 반환
print(len(a))

# 리스트의 멤버 검사 : in / not in
print(10 in a)
print(11 in a)
print(10 not in a)










