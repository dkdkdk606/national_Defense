class Car:
    def __init__(self,color = 'white', speed=0, model='대우'):
        self.color = color
        self.speed = speed
        self.model = model

# 속성 값 조회 메서드 : getter
    def getColor(self):
        return self.color
    def getSpeed(self):
        return self.speed
    def getModel(self):
        return self.model

# 속성 값 변경 메서드 : setter
    def setColor(self, color):
        self.color = color
    def setSpeed(self, speed):
        self.color = speed
    def setModel(self, model):
        self.color = model

    def drive(self):
        self.speed = 50

car = Car()
print('자동차 색상: ', car.getColor())
print('자동차 속도: ', car.getSpeed())
print('자동차 모델: ', car.getModel())
car.setColor('blue')
print('자동차 색상: ', car.getColor())





