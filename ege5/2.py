first = list("аеи")
glas = list("аеи")
sogl = list("бв")
last = list("бвеи")


words = [
    "аиб",
    "ева",
    "бив",
    "иби"
]

for i in words:
    if i[-1] in last and i[0] in first and i[1] in sogl and i[-1] in glas:
        print(i)
