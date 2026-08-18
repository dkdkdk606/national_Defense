# # 4. 문자열을 입력받은 후 문자 o는 $로 변경하여 출력하는 코드를 작성하시오
text = input("문자열을 입력하세요 : ")
print(f'{text.replace("o","$")}')

# # 5. 연/월/일 형식으로 문자열을 입력받아 10년 후 날짜를 예시와 같이 출력하는 코드를 작성하시오
from datetime import date, datetime, timedelta
input_date = datetime.strptime(input("날짜(연/월/일) 입력 : "),'%Y/%m/%d')

after_date = input_date + timedelta(days=365)
print(f'입력한 날짜의 10년 후 => {after_date.year}년{after_date.month}월{after_date.day}일')

# 6. 입력한 숫자만큼 하트문자를 출력하는 코드를 작성하시오.
cnt = input("숫자를 여러개 입력하세요.")
for i in range(len(cnt)):
    for j in range(int(cnt[i])):
        print('\u2665', end="")
    print()

