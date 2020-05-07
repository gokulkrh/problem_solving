a = list(map(int, input().split()))[:4]
c = 0
b = []
for i in a:
    if i not in b:
        b.append(i)
print(4-len(b))