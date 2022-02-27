a,b = 1012, 9638

c = 0
m = 0
start = 1014
end = b+1
step = 3

for n in range(start, end, step):
    if n%3==0 and n%11!=0 and n%13!=0 and n%17!=0 and n%19!=0:
        c+=1
        m = n if n>m else m

print(c, m)
