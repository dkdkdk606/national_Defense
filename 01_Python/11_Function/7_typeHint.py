# 타입힌트 ()
'''
- 변수, 함수의 매개변수, 반환값의 자료형을 코드에 명시하는 방법
- 파이썬은 동적타이핑 언어이므로 타입을 반드시 지정할 필요가 없으나
- 규모가 커질수록 작업을 원활하게 수행하기 위해 타입힌트 사용 권장

자동완성
오류발견
협업
사용이유
    가독성향상
    버그감소
    협업용이
타입힌트가 강제적이지는 않ㅇ므

- 기본 타입힌트 : 파이썬 자료형
    정수 : int
    실수 : float
    문자열 : str
    논리형 : bool
    리스트 : list
    튜플 : tuple
    딕셔너리 : dict
    세트 : set

'''



'''
bin()함수 정의

def bin(number: SupportsIndex, /) -> str

Return the binary representation of an integer.

>>> bin(2796202)
'0b1010101010101010101010'

input()
def input(prompt: object = "", /) -> str

Read a string from standard input. The trailing newline is stripped.

The prompt string, if given, is printed to standard output without a trailing newline before reading input.

If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError. On *nix systems, readline is used if available.
'''

def add(a, b):
    return a+b

print(10, 3)
print(add(3.5, 10))
print(add('a', 'b'))
print(add([1,2], [3,4]))

# 기본타입 힌트
def hello(name:str):
    print(name)

def square(x: float) -> float:
    return x*x


# 문제. 정수에 대해 짝수인지 판단하는 함수 : 반환값은 논리형

def is_even(x: int) -> bool:
    return x%2==0

# 여러 개의 매개변수
def calc(price:int, count:int, discount:float) -> float:
    return price * count * (1-discount)

# 리스트 타입힌트
# 문제. 정수리스트의 요소들을 모두 더한 결과를 반환하는 함수
def avg_list( list1: list[int]) -> float:
    return sum(list1)/len(list1)


list1 = list(range(10))
print(avg_list(list1))

# 문제. 이름 리스트를 하나의 문자열로 변환하는 함수
def join_names(names):
    return " ".join(names)

list2 = ['배병', '병찬', '찬배']
print(join_names(list2))

# 튜플 타입힌트
def student() -> tuple[str, int]:
    return('ㅂㅂㅊ', 13)

# 딕셔너리 타입힌트
def get_score() -> dict[str,int]:
    return {'lee':100, 'choi':90}

# 세트 타입힌트
def get_score() -> set[str]:
    return {'감자', '고구마'}

# typing 모듈을 이용한 타입힌트
'''
    Any : 어떤 자료형도 허용
    Union : 여러 타입 허용
    Optional : 값이 없을수도 있음
    Callable : 함수를 매개변수로 전달


'''

from typing import Any, Union, Optional, Callable

def show(data:Any) -> None:
    print(data)

show(10)
show(3.15)
show('hello')
show([10, 33])

# 여러데이터 유형 허용
def square(x: int | float=10) -> None:
    return x*x
def square(x: Union[int, float]) -> None:
    return x*x

def print_name(name: str|None):
    print(name)
def print_name2(name: Optional[str]):
    print(name)


def hello(name: str='Guest'):
    print(name)
hello()
hello('gg')

def test(data:list[int]) -> dict[str:int]:
    pass

def test(data:list[dict[str:int]]) -> dict[str:int]:
    pass

def add (x:int, y:int):
    return x+y

def calc(func:Callable[[int,int],int],
        a:int, b:int):
    return func(a,b)
def calc2(func, a, b):
    return func(a,b)

print(calc(add, 3, 5))
print(calc2(add, 3, 5))

# calc() # (func: (int, int) -> int, a: int, b: int) -> int
# calc2() # (func: Any, a: Any, b: Any) -> Any

# docstring : 함수의 매개변수와 반환값에 대한 설명문
#   - 코드의 가독성, 유지보수성, 협업효율성 높일 수 있음
#   - 타입힌트와 같이 사용할것을 권장

def avg_list2( list1: list[int]) -> float:
    """
    학생 점수 평균 계산\n
    Args:\n
        scores : 학생 점수 리스트\n
    Returns:\n
        평균점수
    """
    return sum(list1)/len(list1)

# avg_list2()
# (list1: list[int]) -> float
# 학생 점수 평균 계산
# Args:
#     scores : 학생 점수 리스트
# Returns:
#     평균점수

# 문제. 두 정수 또는 실수를 입력받아 곱한 결과를 반환하는 함수
    # : 타입힌트와 docstring을 지정
def multiply( a: int|float, b: Union[int, float]) -> int|float:
    """
        두 수의 곱 계산\n
        Args:\n
            a : 정수 또는 실수\n
            b : 정수 또는 실수\n
        Returns:\n
            두 수의 곱
    """
    return a*b


# 문제 : 정수형 리스트 요소 중 가장 큰 값을 반환하는 함수
def find_max( list1:list[int]) -> int:
    """
        요소 중 가장 큰 값을 반환\n
        Args:\n
            list1 : 정수 요소만을 가지는 리스트\n
        Returns:\n
            리스트 요소 중 가장 큰 값
    """
    return max(list1)


# 문제 : 학생들의 이름과 점수를 저장하는 딕셔너리를 입력받아 평균 점수를 반환하는 함수
student_scores = {'Kim':96, 'Lee':100, 'Choi':80}

def score_avg(scores:dict[str:int]) -> int:
    """
        학생들의 이름과 점수를 저장하는 딕셔너리를 입력받아 평균 점수를 반환\n
        Args:\n
            scores : '학생이름':점수 형태의 딕셔너리\n
        Returns:\n
            평균 점수
    """
    return sum(scores.values())/len(scores)

print(score_avg(student_scores))

# 문제 : 함수를 매개변수로 전달받아 실행하는 함수에 대한 docstiong 추가 정의하고
#       앞에서 작성한 두 수의 덧셈 함수 add(), 곱셈함수 multiply()를 적용하여 실행해보기

def calc(func:Callable[[int|float,int|float],int|float],
        a:int|float, b:Union[int,float]):
# def calc(func:Callable[[int|float,int|float],int|float],
#         *a:int|float):
#  여러개 받는 형태도 가능
    """
        2개의 매개변수를 가진 함수, 인수를 입력받아 해당 함수의 결과값을 반환\n
        Args:\n
            func : 실행시킬 함수\n
            a : func의 인수
            b : func의 인수
        Returns:\n
            해당 함수의 결과값
    """
    return func(a,b)

print(calc(add, 10, 20))
print(calc(multiply, 10, 20))