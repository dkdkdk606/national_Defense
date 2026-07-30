# while문
#  : 조건이 만족 할 때 까지 반복
'''
    while (조건식):
        반복문장들
        반복을 중지할 문장이 필요(조건이 False가 되도록)  => 증감이 있는 ㅕㅇ태

    # 무한루프
    초기값
    while True:
    while 1:
        반복문장들
        반복을 중지할 문장이 필요(조건이 False가 되도록)
'''


# 문제1. 1에서 10사이의 정수들의 합
total = 0
for i in range(10+1):
    total += 1
print(total)

x=0
total = 0
while x <= 10:
    total += x
    x += 1
print(total)

'''
    # for문
    for 변수 in range(시작값, 끝값+1, 증가 간격 값):
        반복문장
    
    # while문
    변수 = 시작값   # 초기화
    while 변수 < 끝값+1
        반복문장
        변수 += 증가 간격 값
'''

# 문제2. 1~100사이의 3의 배수들의 합

# for 문
mul = int(input("배수는? "))
total = 0
for i in range(100+1):
    if i%mul==0:
        total += i
print(f"1부터 100까지의 모든 {mul}의 배수의 합은 {total}입니다.")

# while 문
i = 0
mul = int(input("배수는? "))
total = 0

while i<(100+1):
    if i%mul==0:
        total += i
    i +=1
print(f"1부터 100까지의 모든 {mul}의 배수의 합은 {total}입니다.")

# 문제3. 한자리 정수를 계속 입려가여 입력한 정수를 출력하되 7을 입력하면 종료

num=0
while num != 7:
    num = int(input("한자리 숫자를 입력하세요 : "))
    print(num)

# num = int(input("한자리 숫자를 입력하세요 : "))
# while num != 7:
#     print(num)
#     num = int(input("한자리 숫자를 입력하세요 : "))
# print(num)
# print("입력종료")    
