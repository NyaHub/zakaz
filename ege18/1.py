data = []
ma = 0

for s in open("18-1.csv"):
    row = list(map(int, s.split(';')))
    data.append(row)
    ma += sum(row)

N = len(data)
M = len(data[0])

work = [[0]*M for i in range(N)]
work1 = [[0]*M for i in range(N)]

for row in range(N-1, -1, -1):
    for col in range(M-1, -1, -1):
        work[row][col] = data[row][col] + min(work[row][col+1] if col==M else ma, work[row+1][col] if row==N else ma)
        work1[row][col] = data[row][col] + max(work[row][col+1] if col==M else 0, work[row+1][col] if row==N else 0)

print(work[0][0])
print(work1[0][0])
