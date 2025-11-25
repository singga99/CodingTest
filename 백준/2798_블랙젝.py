import sys

# m을 넘지 않으면서 m에 최대한 가까운 카드 3장의 합

n, m = list(map(int, sys.stdin.readline().strip().split()))
card = sorted(map(int, sys.stdin.readline().strip().split()))

result = 0
result_sum = 0
result_diff = 999999

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            temp_sum = card[i] + card[j] + card[k]
            temp_diff = abs(m - temp_sum)

            if temp_sum > m:
                continue
            
            if result_diff > temp_diff:
                result_diff = temp_diff
                result_sum = temp_sum

print(result_sum)
