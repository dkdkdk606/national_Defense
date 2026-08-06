# 클래스 메서드(class method)
'''
- 인스턴스를 통하지 않고 클래스에서 바로 호출하여 사용
- 메서드 윗줄에 @classmethod 붙여서 구분
- 메서드 첫번째 매개변수로 cls 키워드를 지정
- 메서드 내에서 클래스 변수, 클래스 메서드를 접근할 때 사용

- 형식
    @classmethod
    def 클래스메서드이름(cls, *args):
        코드들
    
호출
    클래스명.클래스메서드이름()


'''

class Car:
    count = 0

    def __init__(self, color="", speed=0):
        self.color = color
        self.speed = speed
        Car.count += 1
        print(f'색상:{self.color}\n속도:{self.speed}\n수량:{Car.count}')

    @classmethod
    def print_count(cls):
        print(f'현재 {cls.count}번째 자동차가 생산되었습니다.')

    @classmethod
    def create(cls):
        #cls() # 인스턴스 생성
        return cls()
        
    def __str__(self):
        return f'색상: {self.color}, 속도: {self.speed}'



car1 = Car()
car2 = Car()

Car.print_count()
car3 = Car.create()
Car.print_count()

print(car1)