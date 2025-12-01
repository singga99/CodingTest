import sys

input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    
    if n <= 2:
        print(2)
        continue

    # 짝수면 다음 홀수 검사
    if n % 2 == 0:
        n += 1
    
    while True:
        i = 3
        isprime = True

        # sqrt(n)까지 홀수만
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                isprime = False
                break
        
        if isprime:
            print(n)
            break

        n += 2
