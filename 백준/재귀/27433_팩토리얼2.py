import sys

input = sys.stdin.readline

n = int(input().strip())

# result = 1
# for i in range(1, n+1):
#     result *= i

# print(result)

def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num-1)
    
print(fact(n))