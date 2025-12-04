import sys

input = sys.stdin.readline

stack = []

n = int(input().strip())
for _ in range(n):
    num = input().strip().split()
    
    if len(num) == 2:
        a, b = map(int, num)
        stack.append(b)

    else:
        a = int(*num)
        if a == 2:
            if stack:
                print(stack.pop())
            else:
                print(-1)
        
        elif a == 3:
            print(len(stack))

        elif a == 4:
            if stack:
                print(0)
            else:
                print(1)

        elif a == 5:
            if stack:
                print(stack[-1])
            else:
                print(-1)