# 1. 딕셔너리를 이용하여 사용자로부터 영어단어와 뜻을 입력받아 사전을 구성하고, 사용자가 입력한단어를 검색하여 뜻을 출력하는 프로그램을 작성하시오

word = ""
dict = {}
while 1:
    word = input("영어 단어 등록 (종료는 quit) : ")
    if word == "quit":
        break
    elif word in dict:
        print(f"{word}는 이미 등록된 단어 입니다.")
    mean = input(f"{word}의 뜻 입력 (종료는 quit) ")
    if mean == "quit":
        break
    dict[word] = mean
    print()

print()

while 1:
    in_word = input("검색할 단어 입력 (종료는 quit) : ")
    if in_word == "quit":
        break
    elif in_word in dict:
        print(f"{in_word}의 뜻은 {dict.get(in_word)}입니다.")
    else:
        print(f"{in_word}는 사전에 없는 단어 입니다.")
    print()
    
print("종료합니다.")

# 2. 다음 중 오류가 발생하는 경우는 고르고, 그 원인을 설명하시오.
# 3번 리스트는 키값에 들어갈 수 없음
# 4번  문자레터럴 형식을 지키지 않음 끝에 ' 필요

# 3.  다음 코드에서 오류가 발생한다. 그 원인을 설명하시오.
# 튜플은 수정 불가능

# 4. 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
t = 1, 2, 3, 4
# 튜플

# 5. 주어진 문제를 해결하기 위한 파이썬 코드를 작성하시오.
# 1) my_variable 이름의 비어있는 튜플 생성
my_variable = tuple()
# 2) 숫자 1 이 저장된 튜플을 생성
my_variable = (1, )

# 3) 변수 t에 'a', 'b', 'c' 세 문자열을 갖는 튜플을 생성
t = ('a', 'b', 'c')
# 4) 3)에서 생성한 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정
t = ('A', 'b', 'c')

# 5) 다음 튜플을 리스트로 변경
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)

# 6) 다음 리스트를 튜플로 변경
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)

# 7) (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만든 후 출력
tuple1 = (1,2,3)
tuple1 += (4,)
print(tuple1)

# 8) 다음 딕셔너리에서 ’B’에 해당하는 값 추출하고 삭제
a = {'A':90, 'B':80, 'C':70}
print(a.pop('B'))

# 6. 파티에 참석한 사람이 다음과 같을 때 세트를 생성하고, 아래 조건에 맞게 출력하는
# 코드를 작성하시오.
partyA = {"Park","Kim","Lee"}
partyB = {"Park", "길동","몽룡"}
# 1) 파티에 참석한 모든 사람은?
print( partyA | partyB )

# 2) 2개의 파티에 모두 참석한 사람은?
print( partyA & partyB )
# 3) 파티 A에만 참석한 사람
print( partyA - partyB )
# 4) 파티 B에만 참석한 사람
print( partyB - partyA )












