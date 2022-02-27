a,b = 1107, 9504

c = 0
m = b
start = a
end = b+1
step = 9 # !!! после наблюдения было принято решение сделать везде шаг равным числу на которое делиться искомое число

for n in range(start, end, step):
    if n%step==0 and n%15!=0 and n%17!=0 and n%7!=0 and n%19!=0:
        c+=1
        m = n if n<m else m

print(c, m)
