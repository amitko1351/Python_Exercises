def cache_decorator(func):
    # A dictionary that stores the key as the parameters
    # and the key as the result
    cache_memory = {}

    def warp(*args):
        nonlocal cache_memory
        if args in cache_memory:
            return cache_memory[args]
        else:
            # Get the return value
            return_value = func(*args)
            # Put it in the memory
            cache_memory[args] = return_value
            # Return the return value
            return return_value
    return warp


@cache_decorator
def fibonaci_element(number_ele):
    """
    Find the fibonaci element in the seris that in the place
    of number_ele
    :param number_ele: the number of element to find
    :return: the fibonaci element in the seris that in the place
    of number_ele
    """
    if number_ele == 0:
        return 0
    elif number_ele == 1:
        return 1
    return fibonaci_element(number_ele-1) + fibonaci_element(number_ele - 2)


def main():
    print(str(fibonaci_element(5)))
    print(str(fibonaci_element(9)))
    print(str(fibonaci_element(100)))


if __name__ == '__main__':
    main()