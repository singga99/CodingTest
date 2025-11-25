lst = [0] * 100     # 메모이제이션

def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    if lst[x] != 0:
        return lst[x]
    else:
        lst[x] = fibo(x-1) + fibo(x-2)
        return lst[x]

print(fibo(50))