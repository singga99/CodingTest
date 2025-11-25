import sys

n = int(sys.stdin.readline().strip())

room = n
room_num = 1

if n == 1:
    print(1)

else:
    room -= 1
    for i in range(1, n+1):
        room -= (6*i)
        room_num += 1
        if room <= 0:
            break

    print(room_num)