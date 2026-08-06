# 실습1. 다음의 조건에 맞는 자동차 클래스를 정의하고 사용하기
'''
클래스명 : Car
속성:
    color : str
    model : str  -> 비공개 필드
    speed : int
    modelNum : str  -> 비공개 필드


    인스턴스 생성시 필드 기본값 지정
    white
    Acron
    0
    사용자가 객체 생성시 입력

메서드 :
    - 각 필드 값 반환, 변경 메서드 정의
    - upSpeed(증가속도) : 현재속도에 입력된 속도를 더해서 속도를 올리는 메서드
    주행속도가 100을 넘으면 메세지 출력(과속)
    - downSpeed(증가속도) : 현재속도에 입력된 속도를 빼서 속도를 올리는 메서드
    -__repr__() 인스턴스 정보 전달
    stop() : 속도를 0으로 변경하여 정지하는 메서드


'''

class Car():
    color = 'white'
    __model = 'Acron'  # 비공개 필드
    speed = 0
    __modelNum = None
    def __init__(self, modelNum: str):
        self.__modelNum = modelNum

    def getColor(self):
        return self.color
    def getSpeed(self):
        return self.speed
    def getModel(self):
        return self.__model
    def getModelNum(self):
        return self.__modelNum


    def setColor(self, color):
        self.color = color
    def setModel(self, model):
        self.model = model
    def setSpeed(self, speed):
        self.speed = speed
    def setModelNum(self, modelNum):
        self.modelNum = modelNum

    def upSpeed(self, speed):
        self.speed += speed
        if self.speed > 100:
            print("과속")

    def downSpeed(self, speed):
        self.speed -= speed

    def __repr__(self):
        return f'''color : {self.color}
model : {self.color}
speed : {self.speed}
nodelNum : {self.__modelNum}'''
        # info = ""
        # info += "color : {self.getColor()}"
        # info += "model : {self.getModel()}"

        # return info
    def stop(self):
        self.speed = 0

car = Car('333')
print(car)

# 실습2. dog 클래스

class Dog():
    def __init__(self,
                 __breed:str,
                 name:str,
                 age:int=None,
                 color:str=None,
                 size:str=None,
                 __state:str="가만히 있는",
                 saturation:int=0,
                 ):
        self.__breed = __breed
        self.name = name
        self.age = age
        self.color = color
        self.size = size
        self.__state = __state
        self.saturation = saturation
        print(f'이름 : {name}, 품종 : {__breed} 인 dog 생성')

        
    def checkSeturation(self):
        if self.saturation > 7:
            saturation = '배불러'
        elif 7 >= self.saturation > 3:
            saturation = '만족스러워'
        else:
            saturation = '배고파'
        print(f'{self.name}이(가) {saturation}합니다. ')

    def getState(self):
        print(f'{self.name}이(가) {self.__state}중 입니다.')
        
    
    def sit(self):
        self.__state = "앉아있는"
        print(f'{self.name}이(가) 앉았습니다.')

    def stand(self):
        self.__state = "서있는"
        print(f'{self.name}이(가) 일어섰습니다.')

    def sleep(self):
        self.__state = "자는"
        print(f'{self.name}이(가) 잠을잡니다. ')
        self.saturation -= 1
        self.checkSeturation()

    def play(self):
        self.__state = "노는"
        print(f'{self.name}이(가) 신나게 놉니다. ')
        self.saturation -= 2
        self.checkSeturation()

    def run(self):
        self.__state = "뛰는"
        print(f'{self.name}이(가) 뛰어다닙니다. ')
        self.saturation -= 2
        self.checkSeturation()
        
    def eat(self):
        self.__state = "먹는"
        print(f'{self.name}이(가) 밥을 먹습니다')
        self.saturation += 2
        self.checkSeturation()


    def __del__(self):
        print(f'이름 : {self.name}, 품종 : {self.__breed} 인 dog 제거')

    def __repr__(self):
        return f'''
        품종 : {self.__breed}
        이름 : {self.name}
        나이 : {self.age}
        색 : {self.color}
        크기 : {self.size}
    '''


dog1 = Dog('진돗개','하니')
print(dog1)
dog1.getState()

'''
- 필드 :
    breed : 품종 str   -> 비공개 필드
    age : 나이 int
    color : 털색 str
    size : 크기 str
- 메서드
    앉다 : sit
    서다 : stand
    자다 : sleep
    먹다 : eat
    놀다 : play
    뛰다 : run

- 인스턴스 생성시
    품좀과 이름은 사용자가 입력하도록 함
    품종과 이름의 dog 생성되었다는 문자열 출력

- 인스턴스 삭제시
    품종과 이름의 dog 삭제되었다는 문자열 출력

- print(인스턴스) 사용하면 dog 인스턴스 정보 출력

'''


