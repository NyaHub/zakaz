first = list("сж")
second = {
"с":list("жбг"),
"ж":list("сз"),
}
third = list("бгз")

words = [
    list("жсг"),
    list("югз"),
    list("сгж"),
    list("жбс")
]

for i in words:
    if i[0] in first and i[1] in second[i[0]] and i[2] in third and i[2]!=i[1]:
        print("".join(map(str,i)))
