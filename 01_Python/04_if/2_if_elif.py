# if~elif~else 문   (다중 if문)
'''
if 조건식1:
    수행문장1
    ...
elif 조건식2:
    수행문장2
    ...
elif 조건식3:
    수행문장3
    ...
else:
    수행문장4
'''

# if ~ if ~ else    (중첩 if문)
'''
    if 조건식1:
        if 조건식2:
            수행문장2
        elif 조건식3:
            수행문장3
    else:
        ....
        
    if 조건식1 and 조건식2:
        수행문장
    else:
        ....
        
'''

# 문제. 정수를 입력하여 양수, 음수, 0을 구분

num = int(input("정수를 입력해주세요."))
if num > 0:
    print("양수입니다.")
elif num < 0:
    print("음수입니다.")
else:
    print("0입니다.")

# 문제2 세 개의 정수를 입력받아 가장 작을 수 출력하기
num1, num2, num3 = int(input('정수1 입력')), int(input('정수2 입력')), int(input('정수3 입력'))
if num1 < num2 and num1 < num3:
    print(f"가장 작은 숫자는 {num1}입니다.")
elif num2 < num3:
    print(f"가장 작은 숫자는 {num2}입니다.")
else:
    print(f"가장 작은 숫자는 {num3}입니다.")

# 문제3. 가위, 바위, 보 게임
# 두 사람(홍길동, 이몽룡)이 각각 가위, 바위, 보 중 하나를 내면 누가 이겼는지 출력하기
hong = input('홍길동은 가위, 바위, 보 중 어느것을 낼까요? ')
lee = input('이몽룡은 가위, 바위, 보 중 어느것을 낼까요? ')
# 차가 -1, 2 일대 지는 상황이고 3차이니 %3 이용해서 묶기 가능
if hong==lee:
    print("비겼습니다.")
elif (hong=='가위' and lee=='보') or (hong=='바위' and lee=='가위') or (hong=='보' and lee=='바위'):
    print('홍길동이 이겼습니다.')
else:
    print('이몽룡이 이겼습니다.')


# 문제4 : 0~100점 사이의 점수를 입력하면 학점 출력
'''
    90점 이상 : A
    80점 이상 : B
    70점 이상 : C
    60점 이상 : D
    60점 미만 : F
'''

raw_score = int(input("점수를 입력하시오.(0~100점)"))

if 100 >= raw_score >= 90:
    grade = "A"
elif raw_score >= 80:
    grade = "B"
elif raw_score >= 70:
    grade = "C"
elif raw_score >= 60:
    grade = "D"
elif raw_score >= 0:
    grade = "F"



# 참고문제. 문제 4에서의 학점을 사용하여 학점에 맞는 점수로 변환하기

# if 'A' <= grade <='D' or grade == 'F':
score = "오류"

if grade == "A":
    score = 5
if grade == "B":
    score = 4
if grade == "C":
    score = 3
if grade == "D":
    score = 2
if grade == "F":
    score = 1


print(f'학점 : {grade}, 점수 : {score}')





# 문제 5. 몸무게와 체중을 입력하여 BMI 지수 계산하고, 다음 기준에 따라 BMI 결과를 출력
'''
참고. BMI 분류
    저체중 : 18.5미만
    정상 : 18.5 ~ 22.9
    과체중 : 23 ~ 24.9
    비만 : 25.0 이상
    고도비만 : 30.0 이상
'''
weight, height = float(input('몸무게를 입력해주세요(kg)')), float(input('키를 입력해주세요(cm)'))/100

bmi = float(f"{weight / height**2:.1f}")
if bmi <18.5:
    bmi_grade = "저체중"
elif bmi <= 22.9:
    bmi_grade = "정상"
elif bmi <= 24.9:
    bmi_grade = "과체중"
elif bmi >= 25.0:
    bmi_grade = "비만"
elif bmi >= 30.0:
    bmi_grade = "고도비만"

print(f'BMI 분류 : {bmi_grade}')