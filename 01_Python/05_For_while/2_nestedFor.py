# 중첩 루프(다중 for문)
#   : for문 안에 for문

for x in range(1,6):
    for y in range(10,16,5):
        print(f'({x},{y})', end=' ')
    print()

# 문제1. 구구단 : 단을 입력하면 해당하는 단의 구구단을 출력
cnt = int(input("단수 입력: "))
for x in range(1,10):
    print(f'{cnt} * {x} = {cnt * x}')

# 문제2. 구구단: 2단에서 9단까지의 구구단 출력
for x in range(1,10):
    for y in range(2,10):
        print(f'{y} x {x} = {y * x}', end="  ")
        # print(f'{y} x {x} = {y * x}', end="\t") -> 텝으로 하면 좀 더 정렬 예쁘게 나옴
    print()

