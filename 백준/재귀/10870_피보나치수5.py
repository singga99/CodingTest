import sys

input = sys.stdin.readline

n = int(input().strip())
fibo = [0] * (n+1)

if n == 0:
    print(0)
elif n == 1 or n == 2:
    print(1)
else:
    fibo[1], fibo[2] = 1, 1
    
    for i in range(2, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    
    print(fibo[n])