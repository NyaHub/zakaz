first = list(map(int,list("123")))
third = list(map(int,list("1234")))
num = [
list(map(int,list("135"))),
list(map(int,list("24")))
]

words = [
    list(map(int,list("4325"))),
    list(map(int,list("1432"))),
    list(map(int,list("1241"))),
    list(map(int,list("3452")))
]

flag = True

for i in words:
    if i[0] in first and i[2] in third:
        for j in range(1,len(i)):
            if not(i[j] in num[i[j-1]%2]):
                flag = False

        if flag:
            print("".join(map(str, i)))
