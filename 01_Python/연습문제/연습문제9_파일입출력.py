# 1. 파일 s.txt에 있는 내용을 읽고
# 결과와 같이 줄단위 기준으로 정렬한 후 그 결과를 출력하는 프로그램 작성

f1 = open(r'C:\Workspaces\01_Python\연습문제\s.txt',"r",encoding='utf-8')

text = f1.readlines()
# text = [ x.strip() for x in f1.readlines() ]
text.sort()
print("".join(text))
f1.close()
'''
f1.close()
f1 = open(r'C:\Workspaces\01_Python\연습문제\s2.txt',"w",encoding='utf-8')
f1.writelines(text)
'''

# 2. Yesterday 가사가 저장되어 있는 텍스트 파일을 읽어 가사에 사용되고 있는 단어들의
# 목록을 알파벳 순서로 출력하고, 각 단어들이 몇 개씩 사용되고 있는지 단어별 개수를
# 출력하는 프로그램 작성
# ∙ 리스트, 세트, 딕셔너리 등의 자료구조를 이용
# ∙ 단어들은 모두 소문자로 변환하여 사용다.

with open(r'C:\Workspaces\01_Python\연습문제\Yesterday.txt', 'r', encoding='utf-8') as f2:

    text = f2.read()
    print(text)
    
    
    word_list = text.split()
    word_list = [ i.lower() for i in word_list]
    print(word_list)
    word_freq = dict()

    for i in word_list:
        word_freq[i] = word_list.count(i)

    sorted_word_freq = { k:word_freq[k] for k in sorted(word_freq)}

    for i, j in sorted_word_freq.items():
        print(f'\'{i}\': {j}')



# 3. 회원명단을 입력받아 저장하거나, 회원명단파일을 열어 저장되어 있는 회원 명단을 출력하는 프로그램 작성

# ∙ 회원명단을 입력받아 파일로 저장하는 함수 작성
#  input_member(input_file명) - 함수의 매개변수는 명단을 저장할 파일명
# - 사용자로부터 명단을 입력받고 저장이 완료된 후 ‘저장되었습니다’를 출력
# - 명단입력은 q키를 누를때까지 계속 작업
def input_member(input_file:str):
    with open(input_file, 'a', encoding='utf-8') as f3:
        while True:
            add_member = input("멤버를 입력하세요.(종료는 q) : ")
            if add_member == "q":
                return
            f3.write(f"\n{add_member}")

# ∙ 사용자가 입력한 파일을 열어서 출력해주는 함수 작성
#  output_member(output_file명) - 함수의 매개변수는 회원명단이 있는 파일명
# - 전달된 파일명을 이용하여 파일에 들어있는 데이터를 출력

def output_member(output_file:str):
    with open(output_file, 'r', encoding='utf-8') as f4:
        print(f4.read())

#  ∙ 메인에서는 실행결과와 같이 선택한 작업에 해당하는 함수를 호출하여 수행
# - q를 입력할 때까지 실행은 무한 반복
# - 사용자에게 ‘저장 1, 출력 2, 종료 q’ 중에서 선택하게 함
# - 전달된 파일명을 이용하여 파일에 들어있는 데이터를 출력

while 1:
    order = input('저장 1, 출력 2, 종료 q : ')
    if order == 'q':
        break
    elif order == '1':
        f_name = input('멤버 명단을 저장할 파일명을 입력하세요. : ')
        input_member(f_name)
    elif order == '2':
        f_name = input('멤버 명단이 저장된 파일명을 입력하세요. : ')
        output_member(f_name)


# 4. csv 모듈의 reader(), writer() 메소들 이용하여, 리스트데이터를 csv파일로 쓰는 함수
# writecsv()와 csv파일을 읽어 리스트데이터를 반환하는 함수 readcsv()를 작성하시오.

import csv

def writecsv(csv_filename, datalist):
    with open(csv_filename, 'r', encoding='utf-8') as f1:
        witer


    pass

def readcsv(csv_filename):
    pass





# with open('12_FileIO/student.csv', 'w', newline="", encoding='utf-8') as f:
#     #                               newline 안쓰면 불러올때 공백줄로 리스트 요소 1개로
#     writer = csv.writer(f)
#     writer.writerow(['이름','국어','영어','수학'])
#     writer.writerow(['홍길동',90,95,88])
#     writer.writerow(['방자',100,56,90])

# # csv 파일 읽기
# with open('12_FileIO/student.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     next(reader) # 첫줄을 건너뜀 - 보통 키값이 많음











# 4. 한 줄에 두 개의 숫자가 저장되어 있는 파일을 읽어
# 와 한 줄의 두 숫자를 더한 후 연산 결과를 파일로
# 내보내는 프로그램 작성
def mu_sum(input_file, file_name:str):
    input_file.read()

# ∙ 파일을 읽어오고 파일에 쓰고, 숫자에 대해 연산
# 하는 기능은 함수 my_sum()을 정의하여 사용
#  my_sum(inputfile 객체, 저장파일명)

# ∙ 메인에서는 해당 함수를 호출해서 수행

