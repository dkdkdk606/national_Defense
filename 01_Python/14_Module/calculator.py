# 계산 모듈

def add(a:int|float, b:int|float) -> int|float:
    return a+b
def sub(a:int|float, b:int|float) -> int|float:
    return a-b
def mul(a:int|float, b:int|float) -> int|float:
    return a*b
def div(a:int|float, b:int|float) -> int|float:
    ''' b = 0 은 불가'''
    if b!=0:
        return a/b 
    else:
        return '0으로 나눌 수 없습니다.'


if __name__ == '__main__':
    a, b = 10, 3
    print(f'{a}+{b} = {add(a,b)}')
    print(f'{a}-{b} = {sub(a,b)}')
    print(f'{a}*{b} = {mul(a,b)}')
    print(f'{a}/{b} = {div(a,b)}')
    print('__name__:', __name__)

# __name__ 변수
    # : 현재 모듈의 이름 또는 __main__값을 저장하고 있는 내장(시스템)변수

    