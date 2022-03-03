last = list("pnto")
firstNotThird = list("prto")
thirdNotLast = list("opt")

words = [
    "port",
    "ttto",
    "ttoo",
    "oopo"
]

for i in words:
    if i[-1] in last and i[-1]!=i[2] and i[0]!=i[2] and i[2] in thirdNotLast and i[0] in firstNotThird:
        print(i)
