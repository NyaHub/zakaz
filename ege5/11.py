num = list("52186")

for i in range(len(num)):
    num[i] = str(int(int(num[i])/2 if int(num[i])%2==0 else int(num[i]) - 1))

print("".join(num[1:-1]))
