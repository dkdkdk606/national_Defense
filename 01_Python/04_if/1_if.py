# if 문

'''
    if 조건식:
        수행문장1
        수행문장2
        ...

    if 조건식:
        수행문장1
    else:
        수행문장2

'''

# 문제. 정수를 입력하여 양수, 음수 구분

num1 = int(input("정수를 입력해주세요."))
# if num1 > 0:
#     print("양수입니다.")
# elif num1 < 0:
#     print("음수입니다.")
# else:
#     print("0입니다.")

if num1 > 0:
    print('양수')
if num1 < 0:
    print('음수')
