import sys

input = sys.stdin.readline

n = int(input().strip())
sang = set(map(int, input().strip().split()))

m = int(input().strip())
card = list(map(int, input().strip().split()))

for c in card:
    if c in sang:
        print(1, end=' ')
    else:
        print(0, end=' ')