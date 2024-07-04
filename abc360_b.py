inp = input()
s = inp.split(" ")[0]
t = inp.split(" ")[1]

# atcoder:
# a, t, c, o, d, e, r

# w goes up till len(s) - 1
for w in range(1, len(s)):
    # this loop checks for splitting and concatenation
    line = ""
    for i in range(1, len(s)+1):
        line += s[i-1]
        if i % w == 0:
            line += "\n"

    print(line)
