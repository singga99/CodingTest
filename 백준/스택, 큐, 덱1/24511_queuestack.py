import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())

a = deque(map(int, input().strip().split()))   # queue인지 stack인지 판별
b = deque(map(int, input().strip().split()))  # 원소가 들어있는 배열
m = int(input().strip())
c = list(map(int, input().strip().split()))   # 삽입할 원소

# for i in range(m):
#     insert = c[i]

#     for j in range(n):
#         if a[j] == 0:
#             pop = b[j]
#             b[j] = insert
#             insert = pop
            
#         else:
#             pop = insert

#     print(pop, end=' ')

# queue는 전부 추가
result = []
for i in range(n):
    if a[i] == 0:
        pop = b[i]
        result.append(pop)

result.reverse()
if len(result) < m:
    result.extend(c[:m-len(result)])

# m보다 더 크게 extend될 경우도 있어서 m까지만 출력
print(*result[:m])