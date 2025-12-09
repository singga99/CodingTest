import sys

input = sys.stdin.readline

n = int(input().strip())
people = []

check = 0
for i in range(n):
    a, b = input().strip().split()
    if a == 'ChongChong' or b == 'ChongChong':
        check = i
        people.append(a)
        people.append(b)

    if check <= i:
        if a in people or b in people:
            people.append(a)
            people.append(b)


print(len(set(people)))