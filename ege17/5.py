a,b = 1606, 9680

c = 0
m = 0
start = a
end = b+1
step = 11

for n in range(start, end, step):
    if n%11==0 and n%17!=0 and n%13!=0 and n%7!=0 and n%19!=0:
        c+=1
        m = n if n>m else m

print(c, m)
