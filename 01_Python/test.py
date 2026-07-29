pos = 0
neg = 0
zero = 0
for i in range(10):
    j = int(input(f"숫자{i}입력 : "))
    if j > 0:
        pos += 1
    elif j < 0:
        neg += 1
    else:
        zero += 1
print('--------------')
print(f'양수: {pos}개')
print(f'음수: {neg}개')
print(f'0  : {zero}개')