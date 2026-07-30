# 8. 월별 매출 합계와 평균계산
# 다음은 한 매장의 월별 매출액이다. 전체 매출 합계, 월평균 매출액, 매출이 1,500,000원 이상인
# 달의 개수를 계산하여 출력하시오. 

sales = [1200000, 1350000, 980000, 1520000, 1680000, 1430000]
sum = 0
cnt = 0
ave = 0
over_150 = 0
for i in sales:
    sum += i
    cnt += 1
    if i >= 1500000:
        over_150 += 1
print(f"전체 매출 합계 : {sum:,.0f}원")
print(f"월평균 매출 : {sum/cnt:,.0f}원")
print(f"150만원 이상인 달 : {over_150}개월")

# 9. 다음과 같이 출력하는 코드를 작성하시오.
for i in range(5, 0, -1):
    for _ in range(0,i):
        print("*",end="")
    print()

for i in range(5, 0, -1):
    for _ in range(i):
        print(" ", end="")
    for _ in range(2*(6-i)-1):
        print("*", end="")
    print()

# for i in range(1,6):
#     print(f'{'*'*(2*i-1):^10}')


# 10. 피보나치 수열을 만드는 프로그램을 작성한다.
# - 피보나치 수열은 0과 1로 시작되며 다음 피보나치 수는 바로 앞의 두수의 합이 된다.
# - 0부터 시작되는 피보나치 수열은 키

cnt = int(input("생성할 피보나치 수의 갯수는? "))
print("0 1", end=" ")
num_0 = 0
num_1 = 1
num_p = 0

for _ in range(cnt):
    num_p = num_0 + num_1
    print(num_p, end=" ")
    num_0 = num_1
    num_1 = num_p

# 11. 10개 정수를 입력받아서 양수, 음수, 0의 개수를 출력하기
pos = 0
neg = 0
zero = 0
for i in range(10):
    j = int(input(f"숫자{i}입력 : "))
    if j > 0:
        pos += 1
    elif j < 0:
        neg += 1
    else:
        zero += 1
print('--------------')
print(f'양수: {pos}개')
print(f'음수: {neg}개')
print(f'0  : {zero}개')