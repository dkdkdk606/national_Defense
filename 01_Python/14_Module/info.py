
# def show_name():
#     name = input("이름입력: ")
#     print(name)

# def show_phone():
#     phone = input("연락처입력: ")
#     print(phone)


# def input_name():
#     with open(r"14_Module\name","a",encoding='utf-8') as f1:
#         name_list = input("이름 입력: ")
#         f1.write(f'{name_list}\n')

# def get_name():
#     with open(r"14_Module\name","r",encoding='utf-8') as f1:
#             if f1.read().strip() == "":
#                 print("이름없음")
#             else:
#                 f1.seek(0)
#                 print(f1.read())
# def main():
#      input_name()
#      get_name()

# def clear_name():
#     if int(input("password?: ")) == 1111:
#          with open(r"14_Module\name","w",encoding='utf-8') as f1:
#                  f1.write('')
#     else:
#          print("비밀번호가 틀렸습니다.")
     

# if __name__ == '__main__':
#      main()


'''
#  - 이름과 연락처를 키보드로 입력받고 출력하는 show_name(), show_phone() 를 가지는 info.py 작성
임포트하여 사용해보기

name 함수
이름 입출력

phone 함수
연락처 입출력
#  [실행결과]
#     이름 입력: 홍길동
#     홍길동


#     연락처입력 : 010-000-1111
#     010-0000-0000

    input_name() 함수
    키보드로 입력받은 이름 저장

    get_name()함수
    저장된 이름 출력
'''
    
name = ''
def show_name():
    '''이름을 키보드로 입력받고 출력하는 함수'''
    name = input('이름 입력: ')
    print(f'{name}입니다\n')
 
def show_phone():
    '''연락처를 키보드로 입력받고 출력하는 함수'''
    print(input('연락처 입력: '))
 
def input_name():
    '''입력받은 이름 저장'''
    global name
    name = input('이름 입력: ')
 
def get_name():
    '''저장된 이름 출력'''
    print('이름없음' if name == '' else name)
 
def main():
    '''input_name() 함수와 get_name() 함수를 차례로 수행하는 함수'''
    input_name()
    get_name()
 
if __name__ == '__main__':
    main()
