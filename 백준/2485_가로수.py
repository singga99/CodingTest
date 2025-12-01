import sys, math

input = sys.stdin.readline

n = int(input().strip())

tree_lst = []
dist_lst = []
for i in range(n):
    tree = int(input().strip())
    if tree_lst:
        dist_lst.append(tree-tree_lst[-1])
    tree_lst.append(tree)
    
gcd = math.gcd(*dist_lst)
print((tree_lst[-1] - tree_lst[0]) // gcd + 1 - n)