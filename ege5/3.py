first = list("ace")
second = {
"a":list("bcd"),
"e":list("bcd"),
"c":list("ae")
}
last = list("cde")

words = [
"cbe",
"add",
"ece",
"ead"
]

for i in words:
    if i[-1] != i[0] and i[0] in first and i[-1] in last and i[1] in second[i[0]]:
        print(i)
