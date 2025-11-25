import sys

input = sys.stdin.readline

n = int(input().strip())
k = list(map(int, input().strip().split()))

'''
# 처음 풀 떄 오답 -> 이건 2칸 씩 띄어져 있는 것만 더해
d = [0] * n

for i in range(n):
    for j in range(i+2, n):
        d[i] = max(d[i], k[i] + k[j])
    
print(max(d))
'''

d = [0] * n
d[0] = k[0]
d[1] = max(k[0], k[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+k[i])

print(d[n-1])