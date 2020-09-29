a = input()
b = input()
ans = ""
for i in range(0,len(a)):
    if a[i]==b[i]=="0" or a[i]==b[i]=="1":
        ans += "0"
    else:
        ans += "1"
print(ans)