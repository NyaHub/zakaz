a,b = 3232, 8299

mi = b
ma = 0
start = a
end = b+1
step = 1

for n in range(start, end, step):
    if (n%2==0 or n%7==0) and n%15!=0 and n%28!=0 and n%41!=0:
        ma = n if n>ma else ma
        mi = n if n<mi else mi

print(mi, ma)
