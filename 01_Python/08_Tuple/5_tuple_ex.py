# 2차원 튜플

tt = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tt, type(tt))

# 2차 튜플 요소 접근
# 0행 2열의 요소?

print(tt[0])
print(tt[0][1])

# 튜플의 모든 요소를 출력하기
for i in range(len(tt)):
# for i in tt:

    for j in range(len(tt[i])):
    # for j in i:
        print(tt[i][j], end=' ')
        # print(j, end=' ')
    print()

'''
[출력결과]
1 2 3
4 5 6
7 8 9
'''

# 문제2. 튜플에 데이터 40을 추가할 수 있는 방법은?
tt = (10, 20, 30)
t_add = 40, 

tt += t_add

print(tt)
# tt = tuple(list(tt) + [40])
# print(tt)

'''
튜플 실무 활용의 예
1. 변경되면 안되는 데이터 저장 : 안정성 보장
    : GPS 좌표, RGB 색상정보, ...

2. 여러 값을 한번에 변환
    : 함수의 변환값

3. 딕셔너리의 키 값
    : immutable

    예. (120, 80) : 'Tank', 

4. 데이터베이스 조회 결과
    : 한 행(row) 표현

5. 여러 변수 동시 할당(언패킹)
    : 코드 간결하게

6. 
'''