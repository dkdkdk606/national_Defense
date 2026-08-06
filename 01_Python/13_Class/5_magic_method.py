# 매직 메서드(magic method)
'''
- 클래스 내부에 미리 정의된 함수들 : __메서드명__(self)
예. 생성자 : __init__(self, *args)
- 특별한 기능을 수행하기 위해 미리 정의된 메서드
- ex) 생성자 : 객체가 생성될 때 파이썬 인터프리터에 의해 자동으로 호출되는 메서드


'''

class Car:
    def __init__(self):
        pass

# 소멸자: 인스턴스를 삭제할 때 자동 호출
#       가비지컬랙션 시점에 호출: 실행시점 예측 어려움
    def __del__(self):
        pass

# 인스턴스를 print()문으로 출력할 때 실행
    def __repr__(self):
        pass

# 인트턴스를 생성했을 때 그 인스턴스 자체를 print()함수로 화면에 출력하면 나오는 값
#  사용자에게 보여줄 문자열 정의
    def __str__(self):
        pass

# 인스턴스 사이의 덧셈 작업(인스턴스 + 인스턴스 할 때 실행되는 메서드)
    def __add__(self, other):
        pass

# 인스턴스 사이의 뺄셈 작업(인스턴스 - 인스턴스 할 때 실행되는 메서드)
    def __sub__(self, other):
        pass
# 인스턴스 사이 곱셈 작업(*)
    def __mul__(self, other):
        pass

# 인스턴스 사이 등호 작업(=)
    def __eq__(self, other):
        pass
# 인스턴스 사이 != 작업
    def __ne__(self, other):
        pass

# 인스턴스 사이 > 작업
    def __gt__(self, other):
        pass
# 인스턴스 사이 >= 작업
    def __ge__(self, other):
        pass
# 인스턴스 사이 < 작업
    def __lt__(self, other):
        pass
# 인스턴스 사이 <= 작업
    def __le__(self, other):
        pass

# 인스턴스 사이에 divmod 수행
    def __divmod__(self, other):
        pass

# 인스턴스 사이에 / 수행
    def __truediv__(self, other):
        pass
        

# Line 클래스 : 선분 클래스
#  속성 : 선의 길이 length
#  메서드 : 두 선의 합, 차, 비교 등

class Line:
    def __init__(self, length):
        self.length = length
        print(f'{self.length}길이의 선분 생성')

    def __del__(self):
        print(f'{self.length}길이의 선분 삭제')

    def __repr__(self):
        return f'선의 길이: {self.length}'

    def __add__(self, other):
        return self.length + other.length
    
    def __sub__(self, other):
        return self.length - other.length
    
    def __eq__(self, other):
        return self.length == other.length
    def __ne__(self, other):
        return self.length != other.length
    def __gt__(self, other):
        return self.length > other.length
    def __lt__(self, other):
        return self.length < other.length
    def __ge__(self, other):
        return self.length >= other.length
    def __le__(self, other):
        return self.length <= other.length

    def __divmod__(self, other):
        return self.length // other.length, self.length % other.length


line1 = Line(100)
line2 = Line(200)

print(line1)
print(f'두 선의 길이의 합: {line1+line2}')
print(f'두 선의 길이의 차: {line1-line2}')
print(divmod(line1,line2))

if line1 < line2:
    print('선분2가 더 길어요')
elif line1 == line2:
    print('두 선분의 길이가 같아요')
else:
    print('선분1이 더 길어요')

del(line2)