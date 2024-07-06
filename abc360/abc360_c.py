N = int(input())
A = input().split(" ")
W = input().split(" ")

total_cost = 0
moved = {}

non_duplicate = [i for i in A if A.count(i) < 2]

for i in range(0, N):
    a = int(A[i])
    w = int(W[i])
    if a not in moved.keys():
        moved[a] = []

    moved[a].append(w)

for k in moved.keys():
    moved[k].sort(reverse=True)
    for i in range(1, len(moved[k])):
        total_cost += moved[k][i]

print(total_cost)
