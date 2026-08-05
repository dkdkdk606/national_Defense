# 파일 쓰기 (출력)
'''
write(문자열) : 문자열을 파일에 쓰기
writelines(리스트) : 리스트를 파일에 쓰기, 줄바꾸기가 자동으로 삽입되지 않음

'''
music ='''
기쁨 뒤에 슬픔이 오는 건
아름다운 마음이야
쫓아내지 말고 품어주어라
아주 예쁜 돌이 된단다

햇빛 뒤에 그늘이 있는 건
사랑스러운 모습이야
밝은 미소를 짓지 않아도
사랑할 이유가 많단다

너의 웃음과 조화로운 너의 눈물

이보다 더 좋은 것은 없어
흐린 날도 화창한 날도 시린 날도
끼우고 나면 다 퍼즐이 될 거야

기쁨 뒤에 슬픔이 오는 건
아름다운 마음이야
겁내지 말고 마주앉아라
찬란한 그림이 된단다

너의 웃음과 조화로운 너의 눈물

이보다 더 좋은 것은 없어
흐린 날도 화창한 날도 시린 날도
끼우고 나면 다 퍼즐이 될 거야

이보다 더 좋은 게 어딨어
슬프고도 외로운 밤이
찾아오지 않는 날
모든 게 애틋할 거야

너의 웃음과 조화로운 너의 눈물

기쁨 뒤에 슬픔이 오는 건
아름다운 마음이야

'''

f2 = open('12_FileIO/akmu.txt', 'w', encoding='utf-8')
f2.write(music)
f2.close()

f2 = open('12_FileIO/akmu.txt', 'r', encoding='utf-8')
print(f2.read())
f2.close()

# 문제. 키보드로부터 입력받은 문자열을 'keyString.txt' 파일로 저장하고, 저장된 파일을 읽어 화면에 출력하기

# text = input("입력할 문자열을 작성하시오.")
# f3 = open(
#     '12_FileIO/keyString.txt',
#     'w',
#     # 'w+',
#     encoding='utf-8',
# )
# f3.write(text)
# f3.close()
# f3 = open(
#     '12_FileIO/keyString.txt',
#     'r',
#     encoding='utf-8'
# )
# # f3.seek(0)
# print(f3.read())
# f3.close()

# answp. 5명의 이름과 성적을 갖는 데이터 파일(score.txt)을 생성
# f4 = open(
#     '12_FileIO/score.txt',
#     'w',
#     encoding='utf-8'
# )
# f4.write("id, name, score\n")
# for i in range(5):
#     name = input('이름 : ')
#     score = input('점수 : ')
#     message = f'{i+1},{name},{score}\n'
#     f4.write(message)
# f4.close()

# f4 = open(
#     '12_FileIO/score.txt',
#     'r',
#     encoding='utf-8'
# )
# print(f4.readlines())
# f4.close()

# f4.seek(0)
# print(f4.read())
# f4.close()


'''
[파일 내용]
id, name, score
1, 홍길동, 100
2, 이순신, 60
3, 강감찬, 80
4, 최영, 90
5, 방자, 80

'''

data = ['id,name,score\n',
        '1,홍길동,100\n',
        '2,이순신,60\n',        
        '3,강감찬,80\n',
        '4,최영,90\n',
        '5,방자,80\n',
]

f4 = open(
    '12_FileIO/score2.txt',
    'w',
    encoding='utf-8'
)
f4.writelines(data)
f4.close()

# 파일쓰기 모드 'a'
fname = '12_FileIO/score2.txt'
f5 = open(fname, 'w')
f5.write("Hello")
f5.close()

f5 = open(fname, 'w')
f5.write("nonono")
f5.close()

f5 = open(fname, 'w')
f5.write("kakaka")
f5.close()

f5 = open(fname, 'r')
print(f5.read())
f5.close()

