import sys

input = sys.stdin.readline

def isprime(num):
    lst = [True] * (num+1)
    lst[0] = lst[1] = False     # 0과 1은 0

    for i in range(2, int(num**0.5)+1): # 루트 num까지만
        if lst[i]:
            for j in range(i*i, num+1, i):
                lst[j] = False

    return [i for i in range(2, num+1) if lst[i]]


t = int(input().strip())
nums = [int(input().strip()) for _ in range(t)]
max_n = max(nums)

prime = isprime(max_n)

# for n in nums:
    
    


# for _ in range(t):
#     n = int(input().strip())
#     lst = isprime(n)
#     cnt = 0 

#     for i in range(len(lst)):
#         for j in range(i, len(lst)):
#             if lst[i] + lst[j] == n:
#                 cnt += 1
#     print(cnt)