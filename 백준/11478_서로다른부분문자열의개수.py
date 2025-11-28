import sys

input = sys.stdin.readline

s = input().strip()

result = set()
for i in range(len(s)+1):
    for j in range(len(s)+1):
        if s[i:j] and s[i:j] not in result:
            result.add(s[i:j])

print(len(result))