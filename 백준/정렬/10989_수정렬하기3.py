'''
[ 계수 정렬(Counting sort) ]

배열에 존재하는 수 개수 세고, 이를 바탕으로 정렬 수행


'''

import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
counter = Counter()

for _ in range(n):
    counter[int(input())] += 1

for number in sorted(counter):
    for _ in range(counter[number]):
        print(str(number))
