a,b = 3201,12876

c = 0
m = 0
start = 3203
end = b+1
step = 4

for n in range(start, end, step):
    if n%4==0 and n%11!=0 and n%13!=0 and n%7!=0 and n%19!=0:
        c+=1
        m = n if n>m else m

print(c, m)
