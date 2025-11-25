import sys
input = sys.stdin.readline

n = int(input().strip())
d = [0] * (n + 1)

d[1] = 1
d[2] = 1

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

cnt = d[n]
cnt2 = n-2
print(cnt, cnt2)