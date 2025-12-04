import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()
    stack = []

    if s == '.':
        break

    for i in s:
        if (not i.isalpha()) and (i != ' ') and (i != '.'):
            if not stack:
                stack.append(i)
            else:
                if (stack[-1] == '(') and (i == ')'):
                    stack.pop()
                elif (stack[-1] == '[') and (i == ']'):
                    stack.pop()
                else:
                    stack.append(i)

    if stack:
        print("no")
    else:
        print("yes")