# 모듈(module)
'''
- 모듈이란?
    함수, 변수, 클래스들을 모아놓은 파일(.py)
    서로 연관된 작업을 하는 코드들의 모임

- 함수 : 특정한 기능을 수행하는 코드 집합
- 모듈 : 함수, 클래스 들을 모아놓은 파일
- 패키지(package) : 여러 모듈을 모아놓은 디렉터리

- 모듈을 사용하는 이유
        - 코드의 재사용(경제적) : 자주 사용되는 함수를 하넌 작성해놓고 여러곳에서 import 해 사용
        - 코드 작성과 관리가 쉬워지고 효율적
            : 코드를 기능에 따라 모듈 단위로 분리하여 설계함으로써
                효율적인 개발과 유지보수가 가능함
        - 독립적인 네임스페이스(이름공간)
            모듈마다 서로 다른 영역이므로, 동일한 이름의 함수나 변수들을 각 모듈에서 사용 가능
        
- 모듈의 종류
    - 표준모듈 : 파이썬 언어패키지 안에 기본적으로 포함되어있는 모듈
        수백개 모듈이 존재
        예 - random, sys, os, pathlib, datetime, glob, pathlib
        
        사용자 정의 모듈 : 개발자가 직접 정의한 모듈
        - 써드파티(third party) 모듈 : 협력업체나 개인이 만들어서 제공하는 모듈
    

'''


# 모듈의 생성 : calculator.py

# 모듈 이용

import calculator

a, b = 10, 4
print(calculator.add(a, b))
print(calculator.add(10,501092))

print('__name__:', __name__)
print('calculator.__name__: =>', calculator.__name__)


# 모듈 임포트 = 모듈 참조
'''
- 모듈 전체 참조 :
    import 모듈명
    import 모듈명 as 별칭

    ex) import pandas
        pandas.read_csv()

        import pandas as pd
        pd.read_csv()

- 모듈 내 함수를 참조할 경우
    모듈명.함수명

    ex) import pandas as pd
    pd.DataFrame()

    import math
    math.pow()

    
- 모듈 내에서 일부만 참조하기
    from 모듈명 import 변수명 or 함수명
    from 모듈명 import 변수명 or 함수명 as 별칭

    ex) from datatime import date

    form 모듈명 import *
    -> *는 __로 시작하는 스페셜 변수나 매직메서드를 제외한 모든 것 참조

'''

# 문제. 이름과 연락처를 출력하는 show_info() 함수를 갖는 모듈 info.py를 작성하고,
#       모듈을 임포트하여 사용해보기


# import info

# name_list = []
# for _ in range(5):
#     info.input_name()
#     name_list.append(info.name)
# print(name_list)
'''
from info import *

name_list = []
for _ in range(5):
    input_name()
    name_list.append(name)
print(name_list)
'''

from info import input_name, show_phone, get_name, name
name_list = []
for _ in range(5):
    input_name()
    name_list.append(name)
print(name_list)


# info.show_name()
# info.show_phone()

# info.main()
# info.clear_name()

'''
#  - 이름과 연락처를 키보드로 입력받고 출력하는 show_name(), show_phone() 를 가지는 info.py 작성
임포트하여 사용해보기

name 함수
이름 입출력

phone 함수
연락처 입출력
#  [실행결과]
#     이름 입력: 홍길동
#     홍길동


#     연락처입력 : 010-000-1111
#     010-0000-0000

'''




