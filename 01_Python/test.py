text = "파이썬재밌어요"
new_text = ""

for i in text[::2]:
    new_text += f'{i}#'
print(new_text[:len(text)])
print(new_text[:-1])



i=-1
new_text = ""
while i > len(text):
    new_text += text[i]
    i -= 1
print(new_text)
