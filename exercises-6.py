def map_function(function_to_run, params):

    # The list of the return values
    return_values = []
    for param in params:
        return_value = function_to_run(param)
        return_values.append(return_value)
    return return_values


def mul(x,y):
    return x*y


def main():
    return_list = map_function(mul, [(2, 3), (5, 2)])
    print(str(return_list))

if __name__ == '__main__':
    main()