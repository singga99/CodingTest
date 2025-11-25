import sys

input = sys.stdin.readline

x = int(input().strip())

table = [0] * (x+1) # x를 1로 만드는데 걸린 최소 연산 횟수 저장

for i in range(2, x+1):
    table[i] = table[i-1] + 1   # table[i-1]의 값(1) + 현재 x가 -1한 값(1)

    if x % 2 == 0:
        table[i] = min(table[i], table[x//2]+1)
    
    if x % 3 == 0:
        table[i] = min(table[i], table[x//3]+1)

    if x % 5 == 0:
        table[i] = min(table[i], table[x//5]+1)
    
print(table[x])