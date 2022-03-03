import string
word = "b265c42gc4"

word = word.replace("c4", "f16")

n = []
cur = 0

for i in word:
    if len(n) < cur + 1:
        n.append("")
    if i in string.digits:
        n[cur] += i
    else:
        cur += 1

for i in n:
    if len(i)==3:
        word = word.replace(i ,"")

print(word)
