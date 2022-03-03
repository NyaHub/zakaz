first = list("ксб")
second = {
"к":list("жб"),
"с":list("жб"),
"б":list("ксз"),
}
third = list("бжс")

words = [
    list("кжс"),
    list("бкз"),
    list("сзж"),
    list("зкс")
]

for i in words:
    if i[0] in first and i[1] in second[i[0]] and i[2] in third and i[2]!=i[1]:
        print("".join(i))
