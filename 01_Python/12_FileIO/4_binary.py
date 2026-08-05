# 이진파일(binary file)
'''
- 이진파일은 글자가 아닌 비트단위로 의미가 있는파일
- 텍스트파일을 제외한 파일
- 음악파일, 이미지, 동영상, 엑셀, ppt, 워드 파일, 실행파일(exe) 등
텍스트로 열었을 때 이상하게 열리면 대부분 이진파일

'''

# notepad.exe 파일을 읽고 쓰기
# src = 'C:/Windows/notepad.exe'
# dst = '12_FileIO/notepad.exe'

# with open(src, 'rb') as fi:
#     with open(dst, 'wb') as fo:
#         while True:
#             data = fi.read(1) # 1바이트씩 읽기
#             if not data:
#                 break
#             fo.write(data)

# 파이썬 객체 파일에 쓰고 읽기
#  : 객체, 클래스 읽고 쓸 때 객체, 클래스는 텍스트파일로 저장하기 어려워서 이진으로 읽고 써야하는데 그 때 pickle 자주 씀!
'''
모듈 : pickle
파일객체쓰기(저장) : pickle.dump(파일이름.pickle, 'rb')
파일객체 읽기 : pickle.load('rb')


'''



import pickle
base_dir = '12_FileIO/'
with open(base_dir + 'list.pickle', 'wb') as f:
    test = [1,2,3,4]
    pickle.dump(test, f)

with open(base_dir + 'list.pickle', 'rb') as f:
    test2 = pickle.load(f)
    print(test2)
    test2.append(100)
    print(test2)













