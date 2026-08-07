# 비공개 속성/메서드
'''
- 비공개 속성 : 속성을 클래스 내부에서만 사용가능
    사용형식 : __속성명

- 비공개 메서드 : 클래스 내부에서만 사용가능한 메서드
    클래스 내부의 다른 메서드가 호출해서 사용
    
- 접근 제어 표시방법 -> 가시성 
=> 필드나 메서드이름 앞에 __를 붙여서 작성 => 이름장식(name mangling)
balance -> public (자유접근, 어디에서나)
_balance -> protected (내부, 상속관계에서만 접근 가능)
__balance -> private (클래스 내부에서만 접근 허용)
    

'''

class Car:


    def __init__(self,color = 'white', speed=0, model='대우'):
        self.__color = color
        self.speed = speed
        self.__model = model

    def getColor(self):
        return self.__color
    # def getModel(self):
    #     return self.__model
    def __modelInfo(self):
        return self.__model

    def setColor(self, color):
        self.__color = color
    def setModel(self, model):
        self.__model = model

    def printInfo(self):
        print('색상 : ', self.__modelInfo())

car = Car()
# print(car.model) # AttributeError: 'Car' object has no attribute 'model'

print(car.getColor())
# print(car.getModel())

car.setColor('green')
car.setModel('현대')

print(car.getColor())
# print(car.getModel())
car.printInfo()

