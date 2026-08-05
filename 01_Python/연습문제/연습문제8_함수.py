# 4. 다음 조건에 맞는 코드들을 작성하시오.

# 1) "비트코인" 문자열을 화면에 출력하는 print_coin() 함수 정의
def print_coin():
    print("비트코인")
# 2) 1)에서 정의한 함수 호출
print_coin()
# 3) 1)에서 정의한 함수 100번 호출
for i in range(100):
    print_coin()
# 4) "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수 정의
#  (조건. 한 줄에 "비트코인" 문자열을 하나씩 출력)
for i in range(100):
    print_coin()
# 5) 두 수를 인자로 입력 받아 곱한 후 그 결과를 반환하는 mul() 함수 정의
def mul(a,b):
    return a*b

print(mul(3,4))
# 6) 소문자 문자열을 인자로 받아 대문자로 변환하여 반환하는 toUpper() 함수 정의
def toUpper(string):
    return string.upper()
print(toUpper("upper"))

# 7) 리스트를 인자로 받아 짝수만 모아 반환하는 pickup_even() 함수 정의
def pickup_even(num_list):
    # return list(filter(lambda i: i%2==0, num_list))
    even_list = []
    for i in num_list:
        if i%2==0:
            even_list.append(i)
    return even_list
print(pickup_even(range(10)))

