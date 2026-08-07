'''
예외
실행 중 방생하는 오류

- 오류(error)
    - 문법적 오류(Syntax Error) 파이썬 문법을 잘못 사용하는 경우 발생하는 오류ㅜ
        키워드 잘못 입력
        if, for, def등에서 :을 빼거나
        블록을 위한 들여쓰기가 일정하지 않거나, 잘못 들여쓰거나
        문법 오류 발생 시 VSCode에서 빨간 밑줄이 그어짐

    - 실행시간에 잘못된 메모리 접근 오류
    - 논리적 오류 : 예상과 다른결과가 나오는 경우
        알고리즘에 문제

    - 사용자의 잘못된 입력 오류

    오류가 발생하면 프로그램은 중단되고 에러 메세지 출력
    - 발생되는 에러의 예
        SyntaxError : 문법 오류
        TypeError
        ValueError : 값을 잘못지정
                문자열 포맷 서식에서 잘못된 값으로 지정한 경우
                print('%d%%' % c)
        NameError : 변수이름이 없는 경우, 변수가 정의되지 않는 경우
        IndexError : 리스트, 문자열, 튜플과 같은 시퀀스형 데이터에서 인덱스 위치를 잘못 지정한 경우
        KeyError : 키값을 설정하지 않거나 잘못된 키값 지정하는 경우
        ZeroDivisionError : 0으로 나눈 경우
        FileNotFoundError : 파일이나 경로가 없는경우
        UnboundLocalError : 지역변수와 관련된 오류
                        += 연산을 사용하여 변수에 값을 할당할 때 초기값이 지정된 후 사용하지 않고
                        바로 사용한 경우
                        (a에 대한 선언 없음)
                        a+=10
        ModoleNotFoundError : 모듈을 임포트 할 때 모듈 이름을 지정하지 않거나
                            잘못된 이름의 오듈을 지정
        OsError : 파일이나 폴더의 경로를 잘못 지정해서 발생
                백슬래스(\)를 두번 사용하지 않고 한 번만 사용한 경우

    
    - 파이썬의 예외(Exception)
        Exception 클래스를 상속받은 다양한 오류를 처리하기 위한 예외 클래스들이 계층적으로 구성되어 있음
        https://docs.python.org/ko/3/library/exceptions.html#BaseException
    

'''






# 문법 오류
# if x > 10 
#     print('홍길동')
# SyntaxError: expected ':'

# TypeError
# print('나이는'+ 23 +'살')
# TypeError: can only concatenate str (not "int") to str

# NameError
# print(a)
# NameError: name 'a' is not defined

# IndexError
# list1 = [1,2,3,4]
# list1[4]
# IndexError: list index out of range

# ValueError
# print('%d%%' % 90)
# ValueError: incomplete format

# UnboundLoaclError
def add():
    a = a + 1

# add()
# UnboundLocalError: cannot access local variable 'a' where it is not associated with a value

# ModoleNotFoundError
# import mymoudule
# ModuleNotFoundError: No module named 'mymoudule'

# FileNotFoundError
# with open('exception.txt', 'r') as f:
#     f.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'exception.txt'

# OSError
# with open('C:\workspaces\01_Python\14_Module\info.py', 'r') as f:
#     f.read()
# OSError: [Errno 22] Invalid argument: 'C:\\workspaces\x01_Python\x0c_Module\\info.py'

a = int(input('숫자1: '))
b = int(input('숫자2: '))

try:
    result = a/b
except:
    print('오류 발생')
else:
    print(f'{a}/{b}={result}')

# 최상위 Exception 지정하여 처리
try:
    result = a/b
except Exception as e:
    print('오류 발생', e)
else:
    print(f'{a}/{b}={result}')


# 에러 종류를 명시하여 처리
try:
    num = int(input('숫자입력:'))
except ValueError as e:
    print('숫자가 아닙니다.')
    print(e)
else:
    print(num)

# 여러 개의 예외 처리문 사용하는 경우
#   : 예외발생 가능한 문장이 여러개 있는 경우 첫번째 예외상황을 만나면 이를 처리하고 프로그램을 정상종료
        # 따라서 뒤의 예외는처리하지 못함(첫번재 에러만 처리됨)

a = [1, 2, 3]

try:
    print(a[len(a)])
    print(10/0)
except ZeroDivisionError as e:
    print("0으로 못나눔", e)
except IndexError as e:
    print("인덱스 범위 벗어남", e)

# 오류 발생 시 아무것도 하지 않고 넘어가기

try:
    f = open('C:/workspace/01_Python/15_Except/error.py', 'r',encoding='utf=8')
except:
    pass
else:
    data = f.read(100)
    print(data)
    f.close()

# 예외 발생 여부와 상관없이 항상 수행되는 블록 finally
try:
    f = open('C:/workspaces/01_Python/15_Except/error.py', 'r',encoding='utf=8')
except:
    pass
else:
    data = f.read(100)
    print(data)
    f.close()
finally:
    print('종료')




