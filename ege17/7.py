a,b = 200, 9120

c = 0
m = b
start = a
end = b+1
step = 8

for n in range(start, end, step):
    if n%8==0 and n%11!=0 and n%17!=0 and n%7!=0 and n%19!=0:
        c+=1
        m = n if n<m else m

print(c, m)
