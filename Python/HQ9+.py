s = input()
q = ['H', 'Q', '9']
c = 0
for i in s:
    if i in q:
        c += 1
if c == 0:
    print("NO")
else:
    print("YES")