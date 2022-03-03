first = list("145")
last = list("1245")
num = [
list("24"),
list("135")
]

words = [
    list(map(int,list("4325"))),
    list(map(int,list("4123"))),
    list(map(int,list("1241"))),
    list(map(int,list("3452")))
]

flag = True
for i in words:
    if str(i[0]) in first and str(i[-1]) in last:
        for j in range(1, len(i)):
            if str(i[j]) in num[i[j-1]%2]:
                flag = False
        if flag:
            print("".join(map(str,i)))
