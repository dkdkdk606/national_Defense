# print() : 출력 함수 (내장(built-in)함수)

print("welcome")
print("1","2")
print("1","2","3", sep="-")  # sep : 구분자(separator) 지정
print("1","2","3", sep="\n", end="+")  # sep : 구분자(separator) 지정, end : 끝 문자 지정
print("1"+"2"+"3")
text = "1"+"2"+"3"
print(text)

addr = "중동"
text = text + addr + "ㅎㅇ"
# 변수 +값, 변수 + 변수 : 변수가 문자열인 경우 하나의 문자열로 결함
print(text)

# 문제 자신의 이름과 나이를 출력하기
name = "배병찬"
age = 34
print("이름 :", name,"\n나이 :", age)

#print(name + age)
print("이름 :" + name + "\n나이 :" + str(age))
#포멧(format) 코드 사용 :   %s,    %f,    $d,   %c,     %x,        %%
#                        문자열, 실수형, 정수형, 문자, 8진수 정수, 16진수 정수
print("이름 : %s\n나이 : %d" %(name, age))
result = "이름 : %s\n나이 : %d" %(name, age)
print(result)

# formet(변수, 형식) 함수
num1 = 10
num2 = 3.14
print(format(num1, '10d'))
print('%10d' % num1)

print(format(num2, 'f'))
print('%f' % num2)
print(format(num2, '15.2f'))
print('%6.2f' % num2)

# %총자리수, 소수점 자리수 f %6.2f 는 총 6자리 차지하는데 소수 2자리까지만 표기

# 문자열.format()
print('num1={0}, num2={1}'.format(num1, num2))
print('num1={1:.2f}, num2={0:3d}'.format(num1, num2))

# fstring을 이용한 포맷
print(f'num2={num2:5.2f}, num1={num1:3d}')
# f 가 붙으면 '' 안에서 {}를 이용해서 변수를 바로 불러올 수 있음 -> 직관적