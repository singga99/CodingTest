import sys

input = sys.stdin.readline

n = int(input().strip())
chat = []
result = 0
for _ in range(n):
    name = input().strip()

    if name == 'ENTER':
        result += len(set(chat))
        chat = []

    else:
        chat.append(name)
    
result += len(set(chat))
print(result)