# 1단계 클래스 선언
# 클래스 선언 시 필드/매서드 작성
class Car:
    color = ' '
    speed = 0

    #메서드 : 기능 정의된 함수
    def drive(self):
        # self : 실제 생성된 인스턴스의 메서드(함수)로 선언
        self.speed = 10
    

# 2단계 인스턴스 생성
car1 = Car()
car2 = Car()
car3 = Car()

# 3단계 : 필드, 메서드 사용

# 인스턴스 생성 후 속성(필드) 추가하여 값 대입
# car1.color = 'red'
# car1.speed = '0'
# car2.color = 'blue'
# car2.speed = '0'
# car3.color = 'green'
# car3.speed = '0'

print(car1.color)
print(car1.speed)
# 메서드 사용
car1.drive()
print(car1.speed)

# 속성 추가
car1.model = "E-Class"

# 속성 값 변경
car1.color = 'red'

# 생성자(constructor) : 객체를 생성해주는 함수
'''
- 생성자는 클래스 이름과 동일
- 생성자는 __init__() 예약함수
    - 클래스이름()을 호출 시 __init__()이 호출되어 객체(인스턴스)를 생성
    - 기본 생성자는 매개변수가 없는 __init__(self) 메서드

- 생성자 형식
def __init__(self, *args):
    초기화할 코드들

'''

class Car2:
    def __init__(self):
        self.color = 'red'
        self.speed = 0

mycar = Car2()
print(f'자동차 색상 : {mycar.color}')
print(f'자동차 속도 : {mycar.speed}')

# 매개변수가 있는 생성자
class Car3:
    def __init__(self,color, speed, model):
        self.color = color
        self.speed = speed
        self.model = model
        # 일반적으로 생성자의 매개변수명은 속성명과 동일하게 사용

car1 = Car3('blue', 0, 'E-Class')
print(f'자동차 색상 : {car1.color}')
print(f'자동차 속도 : {car1.speed}')
print(f'자동차 모델 : {car1.model}')


class Car4:
    def __init__(self,color = 'white', speed=0, model='대우'):
        self.color = color
        self.speed = speed
        self.model = model
    def drive(self):
        self.speed = 50


car1 = Car4()
print(f'자동차 색상 : {car1.color}')
print(f'자동차 속도 : {car1.speed}')
print(f'자동차 모델 : {car1.model}')
car2 = Car4('red')
print(f'자동차 색상 : {car1.color}')
print(f'자동차 속도 : {car1.speed}')
print(f'자동차 모델 : {car1.model}')

mycar = Car4('blue', 0)
print(f'자동차 색상 : {mycar.color}')
print(f'자동차 속도 : {mycar.speed}')
print(f'자동차 모델 : {mycar.model}')

yourcar = Car4(color='blue', model='E-Class')
print(f'자동차 색상 : {yourcar.color}')
print(f'자동차 속도 : {yourcar.speed}')
print(f'자동차 모델 : {yourcar.model}')

theircar = Car4('blue', model='E-Class', speed=10)
print(f'자동차 색상 : {yourcar.color}')
print(f'자동차 속도 : {yourcar.speed}')
print(f'자동차 모델 : {yourcar.model}')

car1.drive()
car2.drive()
print(f'자동차 속도 : {car1.speed}')
print(f'자동차 속도 : {car2.speed}')









