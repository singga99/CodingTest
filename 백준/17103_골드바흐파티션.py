import sys

input = sys.stdin.readline

# 시도 1
# def isprime(num):
#     lst = [True] * (num+1)
#     lst[0] = lst[1] = False     # 0과 1은 0

#     for i in range(2, int(num**0.5)+1): # 루트 num까지만
#         if lst[i]:
#             for j in range(i*i, num+1, i):
#                 lst[j] = False

#     return [i for i in range(2, num+1) if lst[i]]


t = int(input().strip())
nums = [int(input().strip()) for _ in range(t)]
max_n = max(nums)

prime = [True] * (max_n+1)
prime[0] = prime[1] = False

# 에라토스테네스의 체 1번만
for i in range(2, int(max_n**0.5)+1):
    if prime[i]:
        for j in range(i*i, max_n+1, i):
            prime[j] = False

for n in nums:
    cnt = 0

    # n이 6일 경우, (1, 5), (2, 4), (3, 3), (4, 2), (5, 1)
    # 1은 소수 X, 4도 소수 X
    # 두 소수의 순서만 다른 건 하나로 보기 때문에 n//2
    for i in range(2, n//2+1):
        if prime[i] and prime[n-i]:
            cnt += 1

    print(cnt)