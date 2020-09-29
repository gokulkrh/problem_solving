
a = input()
q = []
for i in a:
    if i.isalpha():
        if i not in q:
            q.append(i)
print(len(q))