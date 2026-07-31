# 3. 실행 화면과 같이 7을 입력할 때까지 입력을 반복하고, 7이 입력되면 종료되는 코드를 작성하시오

num3 = input("숫자 입력 : ")
while num != "7":
    num = input("다시 입력 : ")
print('7 입력! 종료')

# 4. 입력받은 십진수를 2진수로 변환하여 출력하기 (※ bin()함수를 사용하지 말 것)


num4 = int(input("십진수 입력: "))
dig = f'{num4 % 2}'
num4_left=num4//2
# print(dig)

print("이진수는 0b", end="")
while num4_left != 0:
    dig = f'{num4_left % 2}' + dig
    # print(dig)
    num4_left=num4_left//2
print(dig)


# 5. 컴퓨터가 생성한 숫자 맞추기 게임
from random import randint
num5 = randint(1,100)
gue = int(input("숫자를 맞혀 보세요.(1~100): "))
while num5 != gue:
    print(f'숫자가 {"높아요" if gue > num5 else "낮아요"}')
    gue = int(input("숫자를 다시 입력하세요: "))
print(f'정답입니다! 입력한 숫자는 {num5}입니다.')

# 6. 6개의 주사위를 동시에 던져 모두 같은 숫자가 나올 때까지 반복해서 던진다. 이때 같은 숫자가 나올 때까지 던진 횟수 출력하기
num6_1, num6_2, num6_3 = 1, 2, 3
cnt = 0
while not(num6_1 == num6_2 == num6_3):
    num6_1, num6_2, num6_3 = randint(1,6), randint(1,6), randint(1,6)
    cnt += 1
    # print(num6_1, num6_2, num6_3)
print(f'주사위 숫자가 모두 같을 때까지 {cnt}번 던졌어요!')
print(f'6개의 주사위의 눈은 모두 {num6_1}')

# 7. 1곡에 2,000원하는 노래방 기계에서 현재 잔액 10000이 소진될 때까지 노래방을 이용하는 프로그램을 작성하시오

cnt = 0
money = 10000
fee = 2000
while money >= fee:
    cnt += 1
    money -= fee
    print(f'노래를 {cnt}곡 불렀습니다.')
    if money < fee:
        break
    print(f'현재 {money}원 남았습니다.')
print("잔액이 없습니다. 종료합니다.")