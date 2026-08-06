# car.py 파일에 정의한 Car 클래스의 인스턴스를 생성


from car import Car

# car = Car('123')
# print(car)

# 클래스 변수 & 인스턴스 변수

#  - 인스턴스 변수 : __init__(self)로 초기화된 변수(인스턴스가 생성될 때 소유하고 있는 변수)
#  - 클래스 변수 : 여러 인스턴스(객체)가 공유하는 변수
#           클래스 정의할 때 가장 앞에 선언
            # 사용할 때 '클래스이름.변수'로 지정하여 사용
'''
- 코드 작성시 변수 선언 위치에 따라 값을 변경할 수 있는 유효범위가 달라지므로
    인스턴스 변수 중 값이 절대로 변경회지 않아야 하거나
    여러 객체들 사이에서 공유되어야 하는 경우는 클래스 변수로 선언하여 사용

'''

class Car2:
    count = 0

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        Car2.count += 1
        print(f'색상:{self.color}\n속도:{self.speed}\n수량:{Car2.count}')

    def __del__(self):
        Car2.count -= 1

car1 = Car2('white', 0)
car2 = Car2('red', 0)
print(car1.count)
print(car2.count)
del(car2)
print(car1.count)









