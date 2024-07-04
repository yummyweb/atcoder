s = input()
# `s` is of length 3, and `s[i]` is one of "R", "M" and "S" indicating rice, miso soup and salad.

found_rice = False
for i in range(0, 3):
    if s[i] == "M":
        if found_rice:
            print("Yes")
        else:
            print("No")

        break

    if s[i] == "R":
        found_rice = True
