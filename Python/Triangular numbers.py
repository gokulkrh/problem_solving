s = 0
n = int(input())
for i in range(1,125251):
    if i*(i+1)//2==n:
        s += 1
if s>0:
    print("YES")
else:
    print("NO")