import sys

n = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().strip().split()))

result = 0

for i in lst:
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    
    if cnt == 2:
        result += 1

print(result)