# 리스트 컴프리헨션
# 문제1. 1부터 10사이 두 정수들의 합의 결과를 리스트로 출력하기

sum_list = [ ]
for i in range(10):
    for j in range(10):
        sum_list.append(f"{i+1} + {j+1} = {i+j}")
print(sum_list)

sum_list2 = [ f'{i} + {j} = {i + j}' for i in range(1, 10+1) for j in range(1,10+1) ]
print(sum_list2)

# 문제2. 메인메뉴 1개와 사이드 메뉴 1개 조합을 모두 구하기
'''
main = ['치킨', '피자', '볶음밥']
side = ['단무지', '피클', '김치']
''' 
main = ['치킨', '피자', '볶음밥']
side = ['단무지', '피클', '김치']

for i in main:
    for j in side:
        print(f'main : {i}, side : {j}')

comp = [ f'main : {i}, side : {j}' for i in main for j in side ]

print()
print("\n".join(comp))

# 리스트 컴프리헨션
result = [(m, s) for m in main for s in side]
print(result, type(result))

# 세트 컴프리헨션
result = {(m, s) for m in main for s in side}
print(result, type(result))

# 딕셔너리 컴프리헨션
result = {m:s for m in main for s in side}
print(result, type(result))