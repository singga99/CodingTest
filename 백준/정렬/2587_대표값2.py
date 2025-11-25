import sys

input = sys.stdin.readline

arr = []
for _ in range(5):
    num = int(input().strip())
    arr.append(num)

arr.sort()
mean = sum(arr) / 5
mid = arr[2]

print(int(mean))
print(mid)