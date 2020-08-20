from algorithm import add_operation, data, find_min
if __name__ == "__main__":
    # solution 1:
    print('problem 1')
    expression_list = add_operation(data)
    result_list = []
    for expression in expression_list:
        result = eval(expression)
        if result == 100:
            print(f'expression: {expression} = {result}')
    # solution 2:
    print('\n\nproplem 2')
    find_min()
