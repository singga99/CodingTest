import sys, math

input = sys.stdin.readline

a, b = map(int, input().strip().split())
print((a*b) // math.gcd(a, b))

    # for i in range(max(a, b), (a*b)+1):
    #     if (i%a == 0) and (i%b == 0):
    #         print(i)
    #         break