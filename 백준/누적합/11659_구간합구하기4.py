import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

# idx 0부터 하나씩 더해가며 전체 합 저장
dp = []
temp = 0
for k in num:
    temp += k
    dp.append(temp)

for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j-1] - dp[i-1] + num[i-1])