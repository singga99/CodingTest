import sys

input = sys.stdin.readline

t = int(input().strip())


for _ in range(t):
    stack = []
    ps = input().strip()
    
    for i in ps:
        if not stack:
            stack.append(i)
            
        else:
            if (stack[-1] == "(") and (i == ")"):
                stack.pop()
            else:
                stack.append(i)

    if stack:
        print("NO")
    else:
        print("YES")