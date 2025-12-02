import sys

input = sys.stdin.readline

m, n = map(int, input().strip().split())

def isprime(a, b):
    lst = [0] * (b+1)

    for i in range(2, b+1):
        lst[i] = i

    for i in range(2, b+1):
        if lst[i] == 0:
            continue

        for j in range(i*i, b+1, i):
            lst[j] = 0

    return [i for i in lst[a:] if lst[i]]
        
result = isprime(m, n)
for i in result:
    print(i)