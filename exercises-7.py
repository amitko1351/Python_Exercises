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
