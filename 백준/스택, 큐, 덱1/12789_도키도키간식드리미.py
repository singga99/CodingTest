import sys

input = sys.stdin.readline

n = int(input().strip())
student = list(map(int, input().strip().split()))

stack = []  # 임시
check = 1

for s in student:
    # 임시 줄의 맨 윗 번호가 check랑 같으면 pop
    while stack and stack[-1] == check:
        stack.pop()
        check += 1

    if check == s:
        check += 1

    else:
        stack.append(s)

# 메인 줄 다 돌고 임시 줄 돌기
while stack and stack[-1] == check:
        stack.pop()
        check += 1

if check == n+1:
     print("Nice")
else:
     print("Sad")