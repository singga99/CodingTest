import sys, math

input = sys.stdin.readline

aa, ab = map(int, input().strip().split())
ba, bb = map(int, input().strip().split())

# 두 분모의 최소공배수
gcd = (ab * bb) // math.gcd(ab, bb)

result_a = (aa * (gcd//ab)) + (ba * (gcd//bb))

# 기약분수
gcd_2 = math.gcd(gcd, result_a)

while True:
    if (gcd % gcd_2 == 0) and (result_a % gcd_2 == 0):
        print(result_a // gcd_2, gcd // gcd_2)
        break