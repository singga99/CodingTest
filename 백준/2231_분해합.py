import sys

n = int(sys.stdin.readline().strip())

result = 0

for i in range(1, n+1):
    num = i
    for j in range(len(str(i))):
        # print(num, i, str(i)[j], j)
        num += int(str(i)[j])
        # print("qqq", num)

    if num == n:
        # print("ffff", num, n)
        result = i
        break
    
    # print(result)

print(result)