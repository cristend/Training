print('Input x:', end='')
x = int(input())
print(f'x:={x}')
print('Input y:', end='')
y = int(input())
print(f'y:={y}')
track_list = []


def find_min(x, y):
    operators = 0
    tmp_y = y
    while True:
        if tmp_y % 2 == 1:
            tmp_y = tmp_y+1
            tmp_y = int(tmp_y / 2)
            operators += 1
            track_list.append(1)
        else:
            tmp_y = int(tmp_y / 2)
        operators += 1
        track_list.append(0)
        if tmp_y <= x:
            break
    sub = x - tmp_y
    operators = operators + sub
    for i in range(sub):
        track_list.append(1)
    return operators


def double(x, y, index):
    print(f'operator {index}: x={x*2} y={y}')
    return x*2


def subtract(x, y, index):
    print(f'operator {index}: x={x-1} y={y}')
    return x-1


print(f'Tracking:\n Input: x={x} y={y}')
operators = find_min(x=x, y=y)
count = 0
while track_list:
    count += 1
    operator = track_list.pop()
    if operator:
        x = subtract(x, y, count)
    else:
        x = double(x, y, count)
print(f'Min operators: {operators}')
