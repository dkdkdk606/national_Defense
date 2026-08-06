# 추상 클래스(abstract class)와 추상 추상메서드(abstract method)
'''
- 추상클래스(abstract class): 직접 객체를 생성하기 위한 클래스가 아니라,
        자식클래스가 따라야할 공통 구조와 규칙을 정의한 클래스
- 추상메서드 : 부모클래스에서는 메서드 이름과 형태만 정의하고
                실제 동작 코드는 자식 클래스에서 정의


- 추상 클래스에서는 직접 객체 생성 불가



- ex) 자동차 클래스 -> 추상클래스
        직접 자동차 인스턴스를 생성하지 않고,
        상속받은 파생(자식)클래스에서 메서드 재정의, 추가 정의하여 인스턴스 생성하여 사용
    Car
        - HybrideCar
        - ElectricCar
        - GasolineCar
        - Truck


'''
# 추상클래스
class Animal:
    def __init__(self, name):
        self.name = name

    # 추상메서드 : 형식만 
    def talk(self):
        raise NotImplementedError('Subclass must implement abstract method!')

# 다형성(polymophism)
# #   : 같은 메서드를 호출하여 객체에 따라 다르게 동작하는 특성
#       1) 상속관계에서의 다형성
#          상속에서 메서드를 오버라이딩과 밀접한 관계가 있는 개념
#          부모클래스의 메서드를 상속받은 자식클래스에서 재정의하므로 다르게 동작하게 함

#       2) 인터페이스와 다형성
#           상속관계가 아닌 객체들이 필요한 메서드를 같은 방식으로 사용할 수 있게 함
#         
class Dog(Animal):
    def talk(self):
        return '멍멍'

class Cat(Animal):
    def talk(self):
        return '냐옹'
    
class Duck(Animal):
    def talk(self):
        return '꽥꽥'


dog = Dog('바둑')
cat1 = Cat('냐옹')
cat2 = Cat('나비')
duck = Duck('노랑')

for animal in [dog, cat1, cat2, duck]:
    print(isinstance(animal, Animal))
    print(f'{animal.name}은 {animal.talk()}')

# 인터페이스와 다형성

class Motorcar:
    def drive(self):
        print('모터자동차로 주행합니다.')

class Bicycle:
    def drive(self):
        print('자전거가 이동합니다.')

vehicles = [Motorcar(), Bicycle()]
for vehicles in vehicles:
    vehicles.drive()

# 3) 산술연산에서 나타나는 다형성
'''
+ 연산자도 자료형에 따라 다르게 동작

'''
print(10+30)
print('10'+'30')
print([1,2,3] + [3,5])


