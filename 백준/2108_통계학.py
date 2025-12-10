import sys
from collections import Counter

input = sys.stdin.readline

# n은 홀수
# 산술평균 - sum(lst)/n
# 중앙값, 최빈값, 범위
n = int(input().strip())
lst = []
for _ in range(n):
    lst.append(int(input().strip()))


print(int(round(sum(lst)/n, 0)))    # 산술평균
print(sorted(lst)[n//2])  # 중앙값

# 최빈값
counter = Counter(lst)
mc = counter.most_common()
mc_max = mc[0][1]   # 최빈값 수 저장

mc_lst = [i for i, v in mc if v == mc_max]
mc_lst.sort()

if len(mc_lst) < 2:
    print(mc_lst[0])
else:
    print(mc_lst[1])

print(max(lst)-min(lst))     # 범위
