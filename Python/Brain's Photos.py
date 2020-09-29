n, m = map(int, input().split())
q = []
c = 0
for i in range(n):
    q.append(input())
for i in q:
    for j in range(0, len(i)):
        if i[j] == 'C' or i[j] == 'M' or i[j] == 'Y':
            c += 1
if c == 0:
    print("#Black&White")
else:
    print("#Color")