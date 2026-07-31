# 날짜/시간 출력 포맷

# 날짜와 시간 관련 모듈 : datetime
# 모듈 : 함수나 변수, 클래스들을 모아 놓은 파일(.py)
#   - 모듈 안에 있는 함수들을 사용하기 위해서는 import문을 사용

from datetime import date, datetime

# import datetime
# print(datetime.date.today())

today = date.today()
print(today, type(today))

year = today.year
month = today.month
day = today.day

print(f'오늘은 {year}년 {month}월 {day}일 입니다.')

print(datetime.today())
print(datetime.now())

cur_time = datetime.now().time()
print(cur_time)
hour = cur_time.hour
minute = cur_time.minute
second = cur_time.second
micro_sec = cur_time.microsecond

print(f'현재시간은 {hour}시 {minute}분 {second}초 {micro_sec}마이크로초')
# 날짜 계산
from datetime import timedelta

today = datetime.today()
print(f'오늘은 {today}')

print(f'어제 : {today + timedelta(days=-1)}')
print(f'내일 : {today + timedelta(days=1)}')

cur_time = datetime.now()
print(f'현재시간 : {cur_time}')
print(f'한시간 전 : {cur_time + timedelta(hours=-1)}')
print(f'한시간 후 : {cur_time + timedelta(hours=1)}')

print(f'2일 3시간 후 : {cur_time + timedelta(days=2, hours=3)}')


# 날짜/시간 출력 형식 지정
today = datetime.today()
cur_time = datetime.now()

print(f'오늘은 {today}')
print(f'현재시간 : {cur_time}')

# Y : 4자리 연도, y : 2자리 연도, H : 24시간, I : 12시간, p:AM/PM
print(today.strftime('%Y-%m-%d %H:%M:%S'))
print(today.strftime('%y-%m-%d %I:%M:%S %p'))

# 문자열로 된 날짜를 날짜 데이터유형으로 변경
str_date = '2026-07-31 10:32:41'
print(type(str_date))
trans_date = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')

print(trans_date, type(trans_date))
print(trans_date.hour)

