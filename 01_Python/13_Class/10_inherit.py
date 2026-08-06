# 클래스의 상속
'''
- 기존의 클래스의 속성과 메서드를 물려받아 사용
- 파이썬의 모든 클래스는 object 클래스에서 상속받아 정의됨
- 상속의 목정
    - 코드의 재사용

- Super(base/부모)클래스 vs Sub(drived/자식)클래스

- 상속 구현 문법

class 클래스명(상속클래스명):
    클래스변수

    def 메서드(self, *args)
        수행코드
    
'''

from car import Car

class Truck(Car):
    def __init__(self, modelNum:str, color:str='white',
                 model : str='Acron', speed : int=0, load:float=1, ):
        super().__init__(color, speed)
        self.load = load

    def drive(self):
        print(f'현재 {self.speed}속도로 {self.load}톤의 짐을 싣고 주행중입니다')
    def loading(self):
        print(f'최대 {self.load}톤의 짐을 운반할 수 있는 트럭')

truck = Truck(modelNum='t211', load=0.5)
print(truck)
truck.loading()