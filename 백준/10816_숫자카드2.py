import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().strip())
sang = Counter(map(int, input().strip().split()))

m = int(input().strip())
card = list(map(int, input().strip().split()))

for c in card:
    print(sang[c], end=' ')