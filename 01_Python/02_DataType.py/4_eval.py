# eval() 함수 문자를 숫자, 식으로 자동 해석해서 값 뽑아줌

x = eval(input('숫자1 입력 : '))
y = eval(input('숫자2 입력 : '))

text = '3+10'
print(f'{x}+{y} = {x+y}')

print(f'{text} => {eval(text)}')

print(f'{eval("3^3")}')