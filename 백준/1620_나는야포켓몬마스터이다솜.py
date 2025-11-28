import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

pocketmon = {}
pocketmon2 = {}
for i in range(n):
    pocketmon[i+1] = input().strip()

# key : value 반대 딕셔너리 생성
pocketmon2 = dict(map(reversed, pocketmon.items()))

test = []
for i in range(m):
    test.append(input().strip())


for t in test:
    if t.isdigit():
        print(pocketmon[int(t)])
    else:
        print(pocketmon2[t])