# with 문
'''
- 파일이나 네트워크 같은 자원을 사용한 뒤 자동으로 정리해주는 문장
with open('파일명', '모드', encoding='인코딩') as 변수명:
    파일객체
'''

fname = '12_FileIO/score2.txt'

data = ['id,name,score,rank\n',
        '1,홍길동,100,1\n',
        '2,이순신,70,4\n',        
        '3,강감찬,80,3\n',
        '4,최영,90,2\n',
        '5,방자,50,5\n',
]
data_str = "".join(data)

# f6 = open(fname, 'w', encoding='utf-8')
# f6.write(data_str)
# f6.close()

# 문제. '12_FileIO/score2.txt'파일의 데이터를 읽어
#        score가 높은 순위로 데이터를 정렬한 데이터파일 result.csv 생성하기

f6 = open(fname, 'r', encoding='utf-8', )
sorted_data = f6.readlines()[1:]

sorted_data = [ x.strip().split(',') for x in sorted_data ]
# for i in range(len(sorted_data)):
#     sorted_data[i] = sorted_data[i].strip().split(",")
    
print(sorted_data)
print('-'*30)
sorted_data.sort(key = lambda x: int(x[2]), reverse=True)
print(sorted_data)

# for i in range(len(sorted_data)):
#     sorted_data[i] = ",".join(sorted_data[i])



f6 = open(fname+"_final", 'w', encoding='utf-8',)
f6.write('id,name,score,rank\n')
for i in sorted_data:
    f6.write(','.join(i) + '\n')
    # for j in i:
    #     f6.write(j+',')
    # f6.write('\n')
f6.close()

f7 = open(fname+"_final", 'r', encoding='utf-8',)
print(f7.read())
f7.close()


# for i in f6.readlines()[1:]:
#     for j in sorted_data:
#         if i[2] > j[2]:
            
#             sorted_data.insert(0,i)
#     temp = i.split(",")
#     sorted_data.append(temp)
#     print(temp)
