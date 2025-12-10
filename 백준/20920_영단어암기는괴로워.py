import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().strip().split())
note = []

for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        note.append(word)

# 우선순위
# 1. 자주 나오는 단어
# 2. 단어 길이 길수록
# 3. 알파벳 사전 순

note_counter = Counter(note).most_common()
note_sorted = sorted(note_counter, key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in note_sorted:
    print(i[0])