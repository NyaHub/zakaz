first = list("абв")
second = list("бвг")
third = list("авг")

words = [
    "агб",
    "ваг",
    "бгг",
    "ббг"
]

for i in words:
    if i[0] in first and i[1] in second and i[2] in third and i[2]!=i[0] and i[2]!=i[1]:
        print(i)
