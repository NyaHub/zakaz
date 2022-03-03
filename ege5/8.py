first = list("бгв")
second = list("абв")
third = list("авг")

words = [
    "агб",
    "ваа",
    "бгв",
    "гба"
]

for i in words:
    if i[0] in first and i[1] in second and i[-1]!=i[0] and i[-1]!=i[1] and i[-1] in third:
        print(i)
