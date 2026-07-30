# 여러줄 문자열

multiline = '''
사과
배
바나나
'''

long_str = '한줄 문자열인데' \
' 한 줄에 표현하기에 너무 긴경우 줄의 마지막에 백슬래쉬를 사용하면 여러 줄로 입력하지만 한 문자열이 된다.'

print(long_str)
print(multiline)

# 문자열 서식 지정(formatting)
# 방법1. 포멧코드 사용 : %s, %d, %f, %c, ...

name = 'Hong'
addr = 'Seoul'
avg = 83.5
total = 350
result = '이름 : %s, 주소 : %s, 총점 : %d, 평균 : %.1f' %(name, addr, total, avg)
print("1 " + result)

# 방법2. format() 함수 사용
result = '이름 : ' + format(name, "s") + ' 주소 : ' + format(addr, "s") + ' 총점 : %d, 평균 : %.1f'%(total, avg)
print("2 " + result)

# 방법3. '문자열 {위치인덱스} '.foramt(변수)
#       '문자열 {변수} '.format(변수 = 값)
#       '문자열 {위치인덱스: 포맷코드} '.format(변수)
result = '이름 : {0}, 주소 : {1}, 총점 : {3}, 평균 : {2}'.format(name, addr, avg, total)
print("3 " + result)
result = '이름 : {}, 주소 : {}, 총점 : {}, 평균 : {}'.format(name, addr, avg, total)
print("4 " + result)

result = '이름 : {name}, 주소 : {addr}, 총점 : {total}, 평균 : {avg}'.format(name='Hong', addr="seoul", avg=33, total=144)
print("5 " + result)

result = '이름 : {0}, 주소 : {1}, 총점 : {3}, 평균 : {2}'.format(name, addr, avg, total)
print("6 " + result)

pi = 3.141592
result = '원주율은 {:10.2f}'.format(pi)
print("7 " + result)

text = '파이썬'
print( '{}'.format(text))




print('-'*20)
text = '파이썬'
print( '{}'.format(text))
print( '{0}'.format(text))
print( '{0:<10}'.format(text))  #전체 10자리 왼쪽 정렬
print( '{0:>10}'.format(text))  #전체 10자리 오른쪽 정렬
print( '{0:^10}'.format(text))  #전체 10자리 가운데 정렬
print( '{0:-^10}'.format(text)) #공백문자 지정
print('-'*20)                   



# 방법4. f-string
#   f'문자열{변수:포맷서식} 문자열'4