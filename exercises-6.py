def map_function(function_to_run, params):

    # The list of the return values
    return_values = []
    for param in params:
        return_value = function_to_run(param)
        return_values.append(return_value)
    return return_values
