# 패키지(package)
'''
- 모듈들을 모아놓은 디렉터리
- 파이썬 모듈은 계층적으로 관리
- 일반 디렉터리와 다름
    - 내부에 __init__.py (빈파일)파일이 존재

- 패키지 사용 방법
    import 패키지명.모듈
    form 패키지명.모듈 import 함수명
    form 패키지명.모듈 import 함수명 as 별칭
    form 패키지명.모듈 import *

    ex) tensorflow.keras.layers.input
        matplotlib.pyplot

'''


# my 디랙터리 안에 pack1, pack2, pack3 생성 후
# 각 디렉터리에 모듈파일 작성
# __init__.py 는 3.3 이후 없어도 무방
'''
mypack/
├── pack1/
│   ├── __init__.py
│   ├── module11.py
│   └── module12.py
├── pack2/
│   ├── __init__.py
│   └── module21.py
└── pack3/
    ├── __init__.py
    └── module31.py


'''


# 패키지 모듈 이용하기
# import mypack.pack1.module11
# mypack.pack1.module11.func11
# 너무 길다...

import mypack.pack1.module11 as m1
m1.func2

from mypack.pack2.module21 import *
func3()

from mypack.pack2 import module21
module21.func4()

from mypack.pack3.mudule31 import func6
func6()


# 모듈에 대한 검색 경로
'''
- 패키지 이용 시 파이썬은 다음의 3가지 장소를 순서대로 돌며 해당 패키지를 찾음
    1. sys.modules      : 모듈이나 패키지를 찾기 위해 가장 먼저 둘러보는 곳
                            import 된 모듈과 패키지를 딕셔너리 형태로 저장하고 있음

    2. built-in modules : 파이썬에서 제공하는 공식 라이브러리들

    3. sys.path         : 파이썬 라이브러리들이 설치된 경로
                            리스트로 구성
'''

import sys

print('sys.path--------------------')
print(sys.path)
print('\nsys.builtin_module_names---------------------------')
print(sys.builtin_module_names)
print('\nsys.modules---------------------------')
print(sys.modules)

'''
ml_project/
├── main.py
└── mlutils/
    ├── __init__.py
    ├── data_loader.py
    ├── preprocessing.py
    ├── metrics.py
    └── model_utils.py
'''






