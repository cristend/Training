data = '123456789'
MAX = len(data)


def add_operation(data):
    index = 1  # index for add operation
    expression_list = []
    count = 0  # correct index each time operation added
    # create all combination of expression
    while True:
        tmp_list = []
        # create all combination of expression from previous expression
        for data in expression_list:
            # prevent adding operation to short expression
            if index+count >= len(data):
                continue
            sum_expression = data[:index+count] + '+' + data[index+count:]
            sub_expression = data[:index+count] + '-' + data[index+count:]
            # * replace for none operator
            none_expression = data[:index+count] + '*' + data[index+count:]
            tmp_list.append(sum_expression)
            tmp_list.append(sub_expression)
            tmp_list.append(none_expression)
        expression_list.extend(tmp_list)
        # seeding expression with only one operation
        tmp_list = [
            data[:index] + '+' + data[index:],
            data[:index] + '-' + data[index:],
            data[:index] + '*' + data[index:]
        ]
        expression_list.extend(tmp_list)
        index += 1
        if index == MAX:
            break
        count += 1
    # remove * from expression and remove duplicate expression
    expression_list = set([x.replace('*', '') for x in expression_list])

    return expression_list


def find_min():
    # input y > x
    # x to equal y by double or subtract 1 per operator
    # output minimal number of operator.
    # x = 7
    # y = 77
    print('Input x:', end='')
    x = int(input())
    print(f'x:={x}')
    print('Input y:', end='')
    y = int(input())
    print(f'y:={y}')
    multi_times = 0
    sub_times = 0
    print('\nTracking:')
    count = 1
    # multi x to higher than half of y
    while x*2 < y:
        x = x*2
        multi_times += 1
        print(f'operator {count}: x={x}, y={y}')
        count += 1
    min_sub = x*2 - y
    left_bound = int(y/2) + 1
    # find left_bound of x to minimal subtract times
    while x > left_bound:
        x -= 1
        sub_times += 1
        print(f'operator {count}: x={x}, y={y}')
        new_min_sub = x*2 - y + sub_times
        min_sub = new_min_sub if new_min_sub < min_sub else min_sub
        count += 1
    # finishing multi x with 2
    x = x * 2
    multi_times += 1
    count += 1
    print(f'operator {count}: x={x}, y={y}')
    # finising subtract 1
    while True:
        if x == y:
            break
        x -= 1
        min_sub += 1
        count += 1
        print(f'operator {count}: x={x}, y={y}')
    # show result
    print(f'So buoc nho nhat de x=y: {multi_times+min_sub}')
    print(f'{multi_times} multi_times and {min_sub} sub_times')
