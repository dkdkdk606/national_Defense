# 인스턴스 메서드(instance method)
'''
- 가장 기본이 되는 클래스의 인스턴스가 가지고 있믐 메서드
- 첫번째 매개변수는 self로 지정해야함 (시스템이 알아서 입력함)


'''
# 정적 메서드(static method)
'''

- 데코레이터 @staticmethod를 이용하여 정의
- self 인자가 필요없는 메서드
- 인스턴스의 속성에 접근 불가
- 주로 유틸리티성 함수를 위한 용도로 사용
- 클래스의 어떤 속성도 변화를 일으키지 않는 함수 => 순수함수
- 클래스 내부에 위치 : 클래스와 연관이 높은 함수를 정의하고 싶을 때
- 클래스명.정적메서드() 로 사용

'''

class Car:
    count = 0

    def __init__(self, color="", speed=0):
        self.color = color
        self.speed = speed
        Car.count += 1
        print(f'색상:{self.color}\n속도:{self.speed}\n수량:{Car.count}')
        if not Car.is_vaild_speed(speed):
            raise ValueError(f"속도는 0~300 사이여야 합니다.")
            # 오류발생 : 적적 속도범위가 아닌 경우
# 인스턴스 메서드
    def drive(self, speed):
        self.speed = speed
        print(f'현재 {self.speed}속도로 주행중입니다')

# 클래스 메서드
    @classmethod
    def print_count(cls):
        print(f'현재 {cls.count}번째 자동차가 생산되었습니다.')

    @classmethod
    def create(cls):
        return cls()

# 정적매서드
# 속도가 허용 범위에 있는지 검사하는 기능
#   : 잘못된 속도를 입력하여 인스턴스 생성시 오류 발생하기 위한 목적
    @staticmethod
    def is_vaild_speed(speed:int) ->bool:
        return 0 <= speed <= 300

    # 연비를 이용해 주행거리 계산
    @staticmethod
    def cal_driving_distance(fual, fual_eff):
        return fual*fual_eff


car1 = Car('red',2300)

distance = Car.cal_driving_distance(fual = 40, fuel_eff=15.2)
print('주행거리 :', distance)
