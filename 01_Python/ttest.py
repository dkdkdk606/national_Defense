# a, b = int(input("숫자 1 입력 : ")), int(input("숫자 2 입력 : "))
# if a>b:
#     k = b
#     b = a
#     a = k

# sum3 = 0
# for i in range( a if a%3==0 else a+(3-a%3) , b-(b%3-1), 3 ):
#     sum3 += i
# print(f'{a} 부터 {b}까지 3의 배수들의 합 : {sum3}')

a, b = int(input("숫자 1 입력 : ")), int(input("숫자 2 입력 : "))
if a>b:
    k = b
    b = a
    a = k

sum3 = 0
for i in range( a + (a%3^3)%3 , b-(b%3-1), 3 ):
    sum3 += i

print(f'{a} 부터 {b}까지 3의 배수들의 합 : {sum3}')

# print((1^3)%3)

# for i in range(10,1,-1):
#     print(i)
'''
00
11

11


01
11

10

10
11

01

'''