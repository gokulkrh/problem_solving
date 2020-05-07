n = int(input())
a = list(map(int, input().split()))[:n]
b = []
for i in a:
    if i not in b:
        b.append(i)
if len(a) == len(b):
    print(a.index(min(a))+1)
else:
    print("still Rozdil")