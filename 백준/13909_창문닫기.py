import sys, math

input = sys.stdin.readline

n = int(input().strip())


'''
1번

def factor(num):
    cnt = 0
    for i in range(1, num+1):
        if num%i == 0:
            cnt += 1
        
    return cnt

result = 0
for i in range(n):
    if factor(i+1) % 2 != 0:
        result += 1

print(result)
'''

# 2번 - 제곱수
print(int(math.isqrt(n)))