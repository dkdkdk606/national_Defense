# CSV 파일 읽고 쓰기
'''
- csv 모듈 이용하여 csv파일을 읽고 쓰기
    import csv

- csv 파일
    : comma separate values 파일

- csv 파일 읽기 : csv.reader(파일객체)
- csv 파일 쓰기 : csv.writer(파일객체)
'''

import csv 

# csv 파일 쓰기

with open('12_FileIO/student.csv', 'w', newline="", encoding='utf-8') as f:
    #                               newline 안쓰면 불러올때 공백줄로 리스트 요소 1개로
    writer = csv.writer(f)
    writer.writerow(['이름','국어','영어','수학'])
    writer.writerow(['홍길동',90,95,88])
    writer.writerow(['방자',100,56,90])

# csv 파일 읽기
with open('12_FileIO/student.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader) # 첫줄을 건너뜀 - 보통 키값이 많음
    for row in reader:
        print(row)

data2 = [['이름','국어','영어','수학'],
         ['홍길동','90','95','88'],
         ['방자','100','56','90'],
]

# csv 파일 쓰기

with open('12_FileIO/student2.csv', 'w',newline="", encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data2)

# csv를 딕셔너리 형태로 읽기

with open('12_FileIO/student.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)