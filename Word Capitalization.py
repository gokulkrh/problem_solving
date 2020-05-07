s = input()

if (len(s) > 0 and s[0].islower()):
    print(s[0].upper() + s[1:])
else:
    print(s)