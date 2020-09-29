q = []
a = list(map(int, input().split()))
for i in range(0,len(a)-1,2):
    q.append(a[i]*a[i+1])
for i in q:
    print(i)