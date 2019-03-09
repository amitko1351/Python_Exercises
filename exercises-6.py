def map_function(function_to_run, params):
    """
    the map function
    :param function_to_run: function to run
    :param params: the parameters to go over
    :return: the return values
    """
    # The list of the return values
    return_values = []
    for param in params:
        return_value = function_to_run(param)
        return_values.append(return_value)
    return return_values


def mul(x):
    return x*x


def main():
    return_list = map_function(mul, [2, 5])
    print(str(return_list))

if __name__ == '__main__':
    main()
