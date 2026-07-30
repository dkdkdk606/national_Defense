# 문자열(string )
'''
    - 문자열의 나열
    - 문자열 생성 : ' ' 또는 " ", ''' ''', """ """
    - 문자열의 특징
        - 순서를 갖는 시퀀스(sequence) 자료형
        - 각 요소를 인덱스(index)를 사용하여 참조
        - 가장 많이 사용하는 자료형
    - 문자열의 연산 ( 시퀀스형 자료에 공통된 연산)
        * 시퀀스형 자료형 : 문자열 리스트 튜플
        - 인덱싱(index) : 문자열 변수명[2]  => 2번 위치(실상 3번쨰)의 값을 가져옴
        - 슬라이싱(slicing) : 문자열 변수명[start : stop : step] => start 부터 stop까지 step 간격 인덱스의 문자만 가져옴
        - 연결하기(concatenate) : + 연산자 사용
        - 반복하기 : * 연산자 => 여러 번 반복해서 하나의 문자열로 결합
        - 멤버검사 : in 연산자 => 어떤 문자가 있는지 검사 True / False
        - 길이정보 : len() 함수 => 문자열의 길이
'''

# 인덱싱
text = 'python'
print(f'text[2] => {text[2]}')
print(f'text[-1] => {text[-1]}')
print(f'text[0] => {text[0]}')
print(f'text[-3] => {text[-3]}')
print(f'text[4] => {text[4]}')

# text[0] = 'P' #안됨 문자열은 부분값 변경 불가(immuable)
print(text)

# 슬라이싱(slicing)부분ㄴ문자열 가져옴
'''
시작:끝
시작:끝:간격
시작:
시작:
'''

text = 'python programming'
print(f'text[3:7] = {text[3:7]}')
print(f'text[3:] = {text[3:]}')
print(f'text[:7] = {text[:7]}')
print(f'text[3:10:2] = {text[3:10:2]}')
print(f'text[:] = {text[:]}')
print(f'text[::2] = {text[::2]}')
print(f'text[::-1] = {text[::-1]}')
print(f'text[7:2:-1] = {text[7:2:-1]}')

text2 = text[:]
print(id(text), id(text2))
text = "hhh"
print(id(text), id(text2))

# 문자열 연결하기 : + 연산자
#   +연산은 좌우항의 데이터 유형이 동일해야 함

name = '홍길동'
adress = '마포구 서교동' 
result = f'{name} + {adress} => {name + " " + adress}'
print(result)
print(name + adress)

# 문자열의 반복 : *연산자

greeting = 'Hi!'
print(greeting * 10)
print('*' * 10)

# 문자열 길이정보 : len()함수
text = 'Python Programming'
print(f'"{text}"의 문자열 길이는 {len(text)}')

#  문자열 멤버 검사 : in / not in 연산자
print('p' in text)
print('P' in text)
print('on' in text)
print('p' not in text)

#문제1. 다음의 문자열의 모든 글자 뒤에 $를 붙여 출력하기
text = 'Python Programming'
new_text = ""
for i in text:
    new_text += i + "$"
print(new_text)
# text = 'Python Programming'
# for ch in text:
#   print(ch, end="$")
# 
# 


# 문제 2 
# 파이썬재밌어요 짝수번째 글자 #으로 바꾸기
text = "파이썬은재밌어요"
new_text = ""
for i in range(len(text)):
    # if i%2 == 1:
    #     new_text += '#'
    # else:
    #     new_text += text[i]
    new_text += text[i] if i%2==0  else '#'
print(new_text)

for i in text[::2]:
    new_text += f'{i}#'
print(new_text[:len(text)])
print(new_text[:-1])



# 문제3 입력받는 문자열열을 거꾸로 출력하기

text = input("문자열을 입력하세요 : ")
# print(text[::-1])
new_text = ""
for i in text:
    new_text = i + new_text
print(new_text)

new_text = ""
for i in range(len(text),0,-1):
    new_text += i
print(new_text)

i=-1
new_text = ""
while i > len(text):
    new_text += text[i]
    i -= 1
print(new_text)

# print(type(range(-5)))

# for i in range(-len(text)):
#     print()
