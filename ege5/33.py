'''
# автомат из задачи для тестов
num = input("first ")
num2 = input("second ")

flag = False
for i in num:
    if int(i) > 6:
        flag = True
        break
if flag:
    print(f"Error in number {num}")
    exit()

for i in num2:
    if int(i) > 6:
        flag = True
        break
if flag:
    print(f"Error in number {num2}")
    exit()

num = sum(list(map(lambda x: int(x, 16), list(num))))
num2 = sum(list(map(lambda x: int(x, 16), list(num2))))

print("".join([str(min(num, num2)), str(max(num, num2)) ]))
'''

def test(x):
    x = list(x)
    if len(x)>2:
        return False

    if int(x[0],16) > 12 or int(x[1],16) > 12:
        return False

    if int(x[0],16) > int(x[1],16):
        return False

    return True

inputs = [
"af",
"410",
"8b",
"76"
]

for i in inputs:
    if test(i):
        print(i)
