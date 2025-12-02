import sys

input = sys.stdin.readline

def isprime(num):
    end = 2*num
    lst = [0] * (end + 1)
    
    for i in range(2, end+1):
        lst[i] = i

    for i in range(2, end+1):
        if lst[i] == 0:
            continue
        for j in range(i*i, end+1, i):
            lst[j] = 0

    return len([i for i in lst[num+1:end+1] if lst[i]])

while True:
    num = int(input().strip())
    if num == 0:
        break

    result = isprime(num)
    print(result)