import sys

n = int(sys.stdin.readline().strip())

if n == 1:
    print()

lst = []
for i in range(2, n+1):
    if n % i == 0:
        while n % i == 0:
            print(i)
            n /= i
