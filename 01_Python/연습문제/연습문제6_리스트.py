# 4
# 1) 회원이름을 입력받아 회원명단 리스트를 생성 하고, 회원명단 리스트의 내용을 출력하는 코드를 완성하시오
member_list = []
for i in range(3):
    member_list.append(input("회원 입력 : "))
print(f'회원 명단 :  {" ".join(member_list)}')

# 2) 상품을 리스트에 추가하고 엔터키를 누르면 입력이 종료되고 등록된 상품 리스트를 출력하는 코드를 작성하시오.

product_list = []
while 1:
    is_enter = input("상품 등록 (엔터키 누르면 종료) : ")
    if is_enter == "":
        break
    product_list.append(is_enter)
print(f'등록된 상품 :  {" ".join(product_list)}')

# 3) 학생들의 점수를 내림차순으로 정렬하여 출력하는 코드를 추가하여 작성하시오.
score_list = []
number_student = int(input("학생 수 입력 : "))
number_of_over_80 = 0
for i in range(number_student):
    score_list.append(int(input(f"학생{i+1} 점수 입력 : ")))
    if score_list[-1] >= 80:
        number_of_over_80 += 1
print(f'총점 : {sum(score_list)}')
print(f'평균 : {sum(score_list)/number_student:.2f}')
print(f'80점 이상 학생 : {number_of_over_80}명')
score_list.sort(reverse=True)
print(f'점수 내림차순 정렬 : {score_list}')

# 4) 사자성어 맞추기 게임을 작성하시오
from random import randint
idioms = ["개과천선", "구사일생", "군계일학", "무용지물", "동고동락", "유비무환", "입신양명", "괄목상대", "막역지우", "고장난명"]
meanings = ["잘못을 고치고 옳은 길에 들어섬", "죽일 고비를 여러 번 겪으며 살아나다", "평범한 사람 가운데 뛰어난 사람", "아무짝에나 쓸모 없는 것", "고통과 즐거움을 함께 한다", "미리 준비해두면 근심 걱정이 없다", "사회적으로 인정받고 출세하여 이름을 세상에 드날림", "다른 사람의 학식이나 업적이 크게 진보한 것을 말함", "생사를 같이 할 수 있는 친밀한 벗", "상대 없이 혼자서는 어떤 일을 이룰 수 없다"]

print("사자성어 맞추기 게임을 시작합니다")
print('-'*32)

ans = ""
select = randint(0, len(idioms)-1)
while 1:
    print(f"{meanings[select]}")
    ans = input('이말의 사자성어는? : ')
    if ans == idioms[select]:
        break
    print('\n틀렸습니다...다시 도전 !\n')
print('\n맞습니다.. 게임을 종료합니다.')
