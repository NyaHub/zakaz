a,b = 3712, 8432

c = 0
m = b
start = a
end = b+1
step = 1

for n in range(start, end, step):
    if (n%2==n%4) and (n%13==0 or n%14==0 or n%15==0):
        c+=1
        m = n if n<m else m

print(c, m)
