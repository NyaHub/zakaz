second = list("234")
last = list("1345")
12345
num = [
list("135"),
list("24")
]

words = [
    list(map(int,list("4321"))),
    list(map(int,list("4123"))),
    list(map(int,list("1241"))),
    list(map(int,list("3452")))
]
for i in words:
    flag = True
    if str(i[1]) in second and str(i[-1]) in last:
        for j in range(1, len(i)):
            if not(str(i[j]) in num[i[j-1]%2]):
                flag = False
        if flag:
            print("".join(map(str,i)))
