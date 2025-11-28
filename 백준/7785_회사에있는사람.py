import sys

input = sys.stdin.readline

n = int(input().strip())

log_list = set()
for i in range(n):
    name, log = input().strip().split()
    
    if log == 'enter':
        log_list.add(name)
    else:
        log_list.remove(name)

for i in sorted(log_list, reverse=True):
    print(i)