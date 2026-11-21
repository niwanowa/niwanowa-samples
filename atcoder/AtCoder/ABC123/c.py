import math
n = int(input())
move_list = [int(input()) for _ in range(5)]
time = 0
time += math.ceil(math.ceil(n/move_list[0]))
if move_list[0] > move_list[1]:
    time = 1 + (math.ceil(n/move_list[1]))
else:
    time = 1 + time
if move_list[1] > move_list[2]:
    time = 1 + (math.ceil(n/move_list[2]))
else:
    time = 1 + time
if move_list[2] > move_list[3]:
    time = 1 + (math.ceil(n/move_list[3]))
else:
    time = 1 + time
if move_list[3] > move_list[4]:
    time = 1 + (math.ceil(n/move_list[3]))
else:
    time = 1 + time
print(time)
