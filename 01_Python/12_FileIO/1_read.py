# 파일입출력
'''
파일입출력 단계
1단계 : 파일열기
        파일객체변수 = open(파일경로, 파일모드)
        파일경로 : 문자열 형식으로 파일의 경로를 지정
                    'data.txt'
                    'C:/data/test.txt' -> 절대경로
        파일모드 : r 읽기 / w 쓰기 / a 뒤에붙여쓰기 | + => 읽기/쓰기 가능
                텍스트파일  r / w / a       r+ / w+ / a+
                이진파일    rb / wb / ab    rb+ / wb+ / ab+

2단계 : 파일처리 (읽기 / 쓰기)
        파일객체변수.read()
        파일객체변수.readline()
        파일객체변수.readlines()
        파일객체변수.write()
        파일객체변수.writeline()

3단계 : 파일닫기

'''
f = open(r'12_FileIO\data.txt', 'r', encoding='UTF-8') # 같은위치 파일이라 이렇게 열기 가능
# f = open('12_FileIO\\data.txt', 'r') 
# data.txt 파일은 한글문자가 utf-8 문자코드로 저장되어있음
text = f.read()
print(text)
f.close()

f = open('12_FileIO\\data.txt', 'r', encoding='UTF-8')
text = f.readline()
print(text)
f.close()

f = open('12_FileIO\\data.txt', 'r', encoding='UTF-8')
while True:
    line = f.readline()
    if not line:
        break
    print(line, end="")

f.close()

f = open('12_FileIO\\data.txt', 'r', encoding='UTF-8')
for line in f.readlines():
    print(line.strip())
f.close


# seek() 메서드 : 파일 포인터의 위치를 원하는 위치로 이동시키는 메서드
#  - 파일은 내부적으로 파일포인터가 존재
#  - 파일포인터는 현재 읽거나 쓸 위치를 가리킴
#  - seek(offset, whence)
        # offset : 이동할 바이트 수
        # whence : 기준 위치(생략 가능)
        #         0 : 파일의 시작(기본값)
        #         1 : 현재 위치
        #         2 : 파일의 끝
f = open('12_FileIO\\data.txt', 'r', encoding='UTF-8')
print(f.read())
# 파일 전체를 읽으면서 포인터가 파일 끝으로 감 -> f.read() 시 "" 반환
print('-'*30)
print(f.read())
f.seek(0)
# 포인터를 다시 시작으로 옮김
print(f.read())

print('-'*30)
f.seek(6)
print(f.read(10))