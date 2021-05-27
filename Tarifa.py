X = int(input())
N = int(input())
total = X

for _ in range(N):
    total = (total - int(input())) + X

print(total)