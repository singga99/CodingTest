import sys

n = int(sys.stdin.readline().strip())

# 줄 찾기
line = 1
for i in range(1, n+1):
    n = n - i
    if n <= 0:
        break
    line += 1

lst = []
for j in range(line):
    lst.append(f"{j+1}/{line-j}")

if line % 2 == 0:
    print(lst[n-1])
else:
    print(lst[-n])