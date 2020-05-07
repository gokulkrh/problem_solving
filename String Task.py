c = ["a","e","i","o","u","y","A","E","I","O","U","Y"]
s = input()
z = list(s)
for i in s:
    if i in c:
        z.remove(i)

for i in range(len(z)):
    z.insert(2*i+1,".")

z.pop(len(z)-1)
z.insert(0,".")
p = ""
for i in z:
    p += i
p = p.lower()
print(p)