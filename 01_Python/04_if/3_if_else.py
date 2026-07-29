# 삼항연산자 사용한 if 문 (한줄 if문)
#   변수 = 참인결과 if (조건식) else 거짓인 결과

# ex) 60점 이상이면 합격, 그렇지 않으면 불합격
score = int(input('점수입력(0~100): '))

if score >= 60:
    result = '합격'
else:
    result = '불합격'
print(f'{score} => {result}')


result = '합격' if score >=60 else '불합격'
print(f'{score} => {result}')