import sys

'''
def w(a, b, c):
    if (a <= 0) or (b <= 0) or (c <= 0):
        return 1
    
    if (a > 20) or (b > 20) or (c > 20):
        return w(20, 20, 20)
    
    if (a < b) and (b < c):
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    
    return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    

input = sys.stdin.readline
while True:
    a, b, c = list(map(int, input().strip().split()))
    if (a == -1) and (b == -1) and (c == -1):
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")

'''

d = [[[0] * 21 for _ in range(21)] for _ in range(21)]

for x in range(21):
    for y in range(21):
        for z in range(21):
            if (x == 0) or (y == 0) or (z == 0):
                d[x][y][z] = 1
            elif (x < y) and (y < z):
                d[x][y][z] = d[x][y][z-1] + d[x][y-1][z-1] - d[x][y-1][z]
            else:
                d[x][y][z] = d[x-1][y][z] + d[x-1][y-1][z] + d[x-1][y][z-1] - d[x-1][y-1][z-1]


input = sys.stdin.readline

result = 0
while True:
    a, b, c = map(int, input().strip().split())
    if (a == -1) and (b == -1) and (c == -1):
        break
    
    if (a <= 0) or (b <= 0) or (c <= 0):
        result = 1

    elif (a > 20) or (b > 20) or (c > 20):
        result = d[20][20][20]
        
    else:
        result = d[a][b][c]
    
    print(f"w({a}, {b}, {c}) = {result}")