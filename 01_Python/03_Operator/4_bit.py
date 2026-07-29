# 비트연산자
#   : 비트별 연산(정수를 2진수로 변환한 수)
'''
    &   : 비트논리곱(and) -> 둘 다 1인 경우에만 1
    |   : 비트논리합(or)  -> 한쪽만 1이라도 1(둘 다 0인 경우만 0)
    ^   : 비트논리적배타합(xor) -> 둘이 같으면 0 서로 다르면 1
    ~   : 비트 부정 -> 1은 0으로, 0은 1로
    <<  : 왼쪽으로 쉬프트(이동)연산  ->  비트를 왼쪽으로 지정한 비트수 만큼 이동
            2^n을 곱한 효과
    >>  : 오른쪽으로 쉬프트(이동)연산  ->  비트를 오른쪽으로 지정한 비트수 만큼 이동
            2^n을 나눈 효과
'''
num1, num2 = 10, 7
print(bin(num1), bin(num2) )
print(num1 & num2)
print(num1 | num2)
print(num1 ^ num2)
print(~num1)
print(5 << 1)
print(8 >> 1)
# 1010     0111

num1, num2 = 0xffff, 0x0000
print(bin(num1), bin(num2) )
print(num1 & num2)
print(num1 | num2)