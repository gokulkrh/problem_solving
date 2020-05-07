a = int(input())
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = []
m = 0

for i in range(1,b[0]+1):
    d.append(b[i])
for i in range(1,c[0]+1):
    d.append(c[i])

for i in range(1,a+1):
    if i not in d:
        m=1
        print("Oh, my keyboard!")
        break

if m == 0:
    print("I become the guy.")