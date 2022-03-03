word = "ayy1yabc55"

word = word.replace("yy", "")
word = word.replace("abc", "")

a = 0
y = 0
for i in range(len(word)):
    if word[i]=="a":
        a = i
    elif word[i]=="y":
        y = i

word = list(word)

word[a], word[y] = word[y], word[a]

print("".join(word))
