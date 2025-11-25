import sys

# 서로 약수면 factor
# 배수면 multiple
# 둘 다 아니면 neither

while True:
    a, b = list(map(int, sys.stdin.readline().rstrip().split()))

    if (a == 0) and (b == 0):
        break

    # 약수
    if b % a == 0:
        print("factor")
    
    else:
        if a % b == 0:
            print("multiple")

        else:
            print("neither")
