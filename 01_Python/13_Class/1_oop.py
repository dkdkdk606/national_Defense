# 객체 지향 프로그래밍(Object Orinted Programming:OOP)
'''
- 객체(object)라고 하는 코드에 함수, 변수를 함께 묶어 재사용 가능하게 만드는 것
- 객체 : 변수 + 함수를 갖는 단위
    - 실재 존재하는 개념이나 사물
    - 변수 -> 속성(attribute) : 필드(field)로 부름    # 클래스 내의 변수를 속성 이라고 부른다
            객체가 가지고 있는 값(속성)
    - 함수 -> 동작/기능/행동(action) : 메서드(method)로 부름
            객체가 동작(작동)하는 코드의 모임
    
    예. 자동차 객체
        - 자동차의 속성(제조사, 제조년도, 모델명, 색상...)
        - 자동차의 기능(주행하다, 주차하다, 정지하다, 속도를 올리다/내리다,...)
    
- 클래스(class)
    : 객체가 가져야 할 기본 정보를 담은 코드
        객체를 만들어내기 위한 설계도
- 인스턴스(instance)
    : 클래스에 의해 실제로 생성된 객체(메모리에 존재)
        어떤 클래스의 객체인지 관계위주로 설명할 때 많이 사용

* 인스턴스와 객체
    인스턴스와 객체는 같은 것을 뜻함
    객체만 지칭할 때는 객체라고 부르고
    클래스와 연관지어 말할 때는 인스턴스라고 부름
        
        

- 클래스 구현 단계
    1단계 : 클래스 선언
        class 클래스명([상위클래스명])
            필드 선언
            메서드 선언
    
    2단계 : 인스턴스 생성 및 호출
        인스턴스 변수 = 클래스명()
    
    3단계 : 필드나 메서드 사용
        인스턴스변수.필드명
        인스턴스변수.필드명 = 값
        인스턴스변수.메서드()

'''

# 자동차 클래스 구현
# 1단계 : 클래스 선언

class Car:
    pass

# 2단계 인스턴스 생성

car1 = Car()
car2 = Car()

print(car1, type(car1), id(car1))
print(car2, type(car2), id(car2))

print(isinstance(car1, Car))

# 파이썬의 클래스들 : int, float, bool, list, tuple, dice ....
a = 10
b = list(range(1,11,2))
c = dict(x=10, y=20)
print( a, b, c)
print(isinstance(a, int))
print(isinstance(b, list))
print(isinstance(c, dict))