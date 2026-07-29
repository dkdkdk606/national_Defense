# 1. 다음 중첩 if문을 elif를 사용하는 코드로 변경하시오.
score=55
if score >= 60 :
    print("합격이다.")
else :
    if score >= 40 :
        print("불합격 이지만 과락은 아닙니다.")
    else :
        print("불합격 이면서 과락입니다.")

score=55
if score >= 60 :
    print("합격이다.")
elif score >= 40 :
    print("불합격 이지만 과락은 아닙니다.")
else :
    print("불합격 이면서 과락입니다.")


# 2. 정수 3개를 입력받아 제일 큰 수 출력하기
int1 = int(input("정수1 입력 : "))
int2 = int(input("정수2 입력 : "))
int3 = int(input("정수3 입력 : "))

if int1 > int2 and int1 > int3:
    max_v = int1
elif int2 > int3:
    max_v = int2
else:
    max_v = int3
print(f"제일 큰 수 : {max_v}")

# 3. 도형을 선택해서 면적 구하기
dia = input("도형 입력(1: 사각형, 2: 삼각형, 3: 원 : )")
if dia == "1":
    width = int(input("가로 입력 : "))
    lenght = int(input("세로 입력 : "))
    print(f"사각형의 면적 = {width * lenght:.2f}")
if dia == "2":
    width = int(input("밑변 입력 : "))
    lenght = int(input("높이 입력 : "))
    print(f"삼각형의 면적 = {width * lenght / 2:.2f}")
if dia == "3":
    radius = int(input("반지름 입력 : "))
    print(f"원의 면적 = {3.141592 * radius**2:.2f}")

# 4. 가위바위보 게임하기
hong = input('홍길동 입력 : ')
lee = input('이몽룡 입력 : ')
# 차가 -1, 2 일대 지는 상황이고 3차이니 %3 이용해서 묶기 가능
if hong==lee:
    print("비겼습니다.")
elif (hong=='가위' and lee=='보') or (hong=='바위' and lee=='가위') or (hong=='보' and lee=='바위'):
    print('홍길동이 이겼습니다.')
else:
    print('이몽룡이 이겼습니다.')

# 5. 지불 방식에 따른 할인율 계산하기
num = int(input("번호 입력 (1.현금 2.카드) : "))
if num==1 or num==2:
    if num == 1:    
        pay = int(input("지불액 입력 : "))
        discount_r = 0.1
    else:
        pay = int(input("지불액 입력 : "))
        discount_r = 0.05
    print(f"할인률 {discount_r * 100:.0f}%")
    print(f"할인액 : {discount_r * pay:.0f}원")    

else:
    print("잘못 입력하였습니다. 종료합니다.")

# 6. 16진수 글자 하나를 입력하면 16진수인지 아닌지를 구분하며 16진수인 경우 10진수로 변환하여 출력하는 프로그램 작성
hex_c = input("16진수 한 글자 입력 : ")
if 'a' <= hex_c <= 'f' or 'A' <= hex_c <= 'F':
    print(f"10진수 ==>   {int(hex_c,16)}")
else:
    print("16진수가 아닙니다.")