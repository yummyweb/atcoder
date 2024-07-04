inp = input()
s = inp.split(" ")[0]
t = inp.split(" ")[1]

# atcoder:
# a, t, c, o, d, e, r

found = False

# w goes up till len(s) - 1
for w in range(1, len(s)):
    # this loop checks for splitting and concatenation
    line = []
    new = ""
    for i in range(1, len(s)+1):
        new += s[i-1]
        if i % w == 0 or i == len(s):
            line.append(new)
            new = ""

    for i in range(0, w):
        res = ""
        for l in line:
            if len(l) >= i+1:
                res += l[i]

        if res == t:
            found = True

if found:
    print("Yes")
else:
    print("No")
