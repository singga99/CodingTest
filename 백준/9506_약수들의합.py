import sys

while True:
    n = int(sys.stdin.readline().strip())

    if n == -1:
        break

    lst = []
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)

    if sum(lst[:-1]) != n:
        print(f"{n} is NOT perfect.")
    else:
        print(f"{lst[-1]} = " + " + ".join(map(str, lst[:-1])))