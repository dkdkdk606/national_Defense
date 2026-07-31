# 문자열 관련 메서드(method)
# 메서드 : 객체의 함수
#   객체명.메서드이름()

'''
- 문자열 대소문자 변환 : upper(), lower(), swapcase(), title(), capitalize()
- 문자열 검색 : count(), find(), rfind(), index(), rindex(), stratswith(), endswith()
- 문자열 편집 & 치환 : strip(), rstrip(), lstrip(), replace()
- 문자열 분리 & 결합 : split(), rsplit(), join(), splitlines()
- 문자열 정렬 : ljust(), rjust(), center()
- 문자열 판단 : isdigit(), isnumeric(), isdecimal(), isalpha(), isalnum(), islower(), isupper()
                isspace(), istitle(), isidetifier()

'''

# - 문자열 대소문자 변환 : upper(), lower(), swapcase(), title(), capitalize()
text = 'I like python programming. you too? \n i have no idea'
print(f'text.upper() => {text.upper()}')
print(f'text.lower() => {text.lower()}')
print(f'text.swapcase() => {text.swapcase()}')
print(f'text.title() => {text.title()}')
print(f'text.capitalize() => {text.capitalize()}')
print('-'*30)

# - 문자열 검색 : count(), find(), rfind(), index(), rindex(), stratswith(), endswith()
text = 'I like programming, I like swimming' 
print(f'text : {text}')
result = text.count('like')
print(f'text.count(\'like\') => {text.count('like')}')
result = text.find('like')  # 첫 like가 시작되는 인덱스 반환
print(f'text.find(\'like\') => {text.find('like')}')

result = text.find('like',3)  # index 3 이후 부터 찾아 like가 시작되는 인덱스 반환
print(f'text.find(\'like\',3) => {text.find('like',3)}')
result = text.rfind('like')  # 우측 기준으로 가장 먼저 나오는 문자열 찾아 인덱스 변환
print(f'text.rfind(\'like\') => {text.rfind('like')}')
result = text.index('like')  # 가장 먼저 나오는 문자열 찾아 인덱스 변환 없으면 에러
print(f'text.index(\'like\') => {text.index('like')}')
result = text.rindex('like')  # 우측 기준 가장 먼저 나오는 문자열 찾아 인덱스 변환 없으면 에러
print(f'text.rindex(\'like\') => {text.rindex('like')}')

text = 'I like programming, I like swimming'
print(f"text : {text}")
result = text.startswith("I like")  # 'I like'로 시작하는지 확인
print(f"text.startswith('I like') => {text.startswith('I like')}")
result = text.startswith("like", 2)  # index 2 이후부터 'like'로 시작하는지 확인
print(f"text.startswith('like', 2) => {text.startswith('like', 2)}")

result = text.endswith("swimming")  # 'swimming'으로 끝나는지 확인
print(f"text.endswith('swimming') => {text.endswith('swimming')}")
result = text.endswith("swimming",0,20)  # index 0 이후부터 20 미만까지 'swimming'로 끝나는지 확인
print(f"text.endswith('swimming', 0,20) => {text.endswith('swimming', 0,20)}")


# - 문자열 편집 & 치환 : strip(), rstrip(), lstrip(), replace()
text = '     I like programming, I like swimming I like 사과~~~     '
print(text)
result = text.strip() # 양쪽의 공백을 제거
print(f'text.strip() => {text.strip()}')
result = text.lstrip() # 왼쪽의 공백을 제거
print(f'text.lstrip() => {text.lstrip()}')
result = text.rstrip() # 오른쪽의 공백을 제거
print(f'text.rstrip() => {text.rstrip()}')

text = '<span>ㅎㅎ 파이썬 만세'
print(f'text={text}')
result = text.strip('<>')
print(f'text.strip(\'<>\') => {result}')

result = text.strip('ㅎ')
print(f'text.strip(\'ㅎ\') => {result}')

result = text.replace('ㅎ',"")
print(f'text.replace(\'ㅎ\',"") => {result}')


# - 문자열 분리 & 결합 : split(), rsplit(), join(), splitlines()
text = '     I like programming, I like swimming I like 사과~~~     '
print(f'text={text}')
# result = text.split()   # 괄호 안 문자를 기준으로 문자열 분리하여 공백이 아닌 문자열들의 리스트 반환
# print(f'text.split() => {result}')
result = text.split(",")
print(f'text.split(",") => {result}')

text = 'abcd.txt'
result = text.split(',')
print(f"text.split(',') -> {result}")

text = 'one:two:three:four:five'
result = text.split(':')
print(f"text.split(':') -> {result}")
result = text.split(':',2)
print(f"text.split(':',2) -> {result}")


result = "  ".join(result)  # join 앞에 지정한 문자열로 문자열 리스트를 하나의 문자열로 결합
print(f'result = result.join(" ") => {result}')

result = result.split()
result = "-".join(result)  # join 앞에 지정한 문자열로 문자열 리스트를 하나의 문자열로 결합
print(f'result = result.join(" ") => {result}')

text = '''   I like programming,
I like swimming
I like 사과~~~~         '''
print(f'text={text}')
result = text.splitlines()
print(f'result = text.splitlines() => {result}')

# - 문자열 정렬 : ljust(), rjust(), center()
text = 'I like programming,'
print(f'text : {text}, len(text) : {len(text)}')
result = text.center(30)
print(f'text.center(30) => |{result}|')

result = text.ljust(30)
print(f'text.ljust(30) => |{result}|')
result = text.rjust(30)
print(f'text.rjust(30) => |{result}|')

result = text.center(40,"#")
print(f'text.center(40,"#") => |{result}|')



# - 문자열 판단 : isdigit(), isnumeric(), isdecimal(), isalpha(), isalnum(), islower(), isupper()
#                 isspace(), istitle(), isidetifier()

print('1234'.isdigit())
print('1234\u2155\u2156', '1234\u2155\u2156'.isdigit())
print('1234\u2155\u2156', '1234\u2155\u2156'.isnumeric())
print('123\u0663', '123\u0663'.isdecimal())
print('123', '123'.isdecimal())
print('abc한글', 'abc한글'.isdecimal())
print('abc', 'abc'.isdecimal())
print('1abc한글', '1abc한글'.isdecimal())
print('abc한글'.isalpha())
print('1abc한글'.isalpha())

print('123,abc한글'.isalpha())
print('abc'.islower())
print('abc'.isspace())
print('\t \r \n'.isspace())
print( 'True is'.isidentifier())
print('False'.isidentifier())

# 문제. 다음의 문장에서 like가 있는 인덱스를 모두 찾아 출력하기

text = 'I like programming, I like swimming I like 사과~~~ I like kiwi!'
like_index = 0
while 1:
    like_index = text.find('like', like_index)
    if like_index == -1:
            break
    print(text.find('like', like_index))    
    like_index = text.find('like', like_index) + 1

    