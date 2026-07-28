# input() 함수
#  : 표준입력 장치로부터 입력을 받는 함수 (내장함수)
#  변수 = input("프롬프트 문자열")
# 프롬프트 문자열 생략 가능
# 입력값은 문자열로 저장


name = input("너의 이름은: ")
age = input('나이는: ')
print(name + " 바보 벌써 " + age + "살 이래요~")
print(type(name), type(age))

# 연습문제1. 두 정수를 입력받고 합계 출력하기

num1 = input("a 값은?")
num2 = input("b 값은?")
print(f'{num1} + {num2} = {float(num1)+float(num2)}')

# 연습문제2. 3과목의 점수를 입력받아 총점과 평균을 계산하여 출력하기
'''



'''
score_korean = input("국어점수 : ")
score_korean = float(score_korean)
score_english = input("영어점수 : ")
score_english = float(score_english)
score_math = input("수학점수 : ")
score_math = float(score_math)

print(f'총점은 {score_korean+score_english+score_math}점, 평균 점수는 {(score_korean+score_english+score_math)/3}입니다.')

# 몸무게와 키 입력 받아 BMI 지수 계산하여 출력하기
# BMI 지수 계산식: 몸무게 / 키**2 (키는 m 단위)

weight = float(input('당신의 몸무게는? (kg) :'))
height = float(input('당신의 키는? (cm) :'))/100

print(f'당신의 bmi는 {weight / height**2:.2f}')

