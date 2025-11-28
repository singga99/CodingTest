import sys

input = sys.stdin.readline
n = int(input().strip())

arr = list(map(int, input().strip().split()))
sort_arr = sorted(set(arr))
index_dic = {}

for i in range(len(sort_arr)):
    index_dic[sort_arr[i]] = i

for i in arr:
    print(index_dic[i], end=' ')