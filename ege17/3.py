a,b = 1100, 11000

c = 0
m = 0
start = a
end = b+1
step = 1

for n in range(start, end, step):
    if n%6==0 and n%7!=0 and n%13!=0 and n%17!=0 and n%23!=0:
        c+=1
        m = n if n>m else m

print(c, m)
