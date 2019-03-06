def compress_string(string):
    """
    the function compress the string
    :param string: string to compress
    :return: the new compressed string
    """
    # If there is no string return None
    if not string:
        return None
    # Last char in the string
    last_char = string[0]
    # Count the number of repetition
    count_repet = 0
    # String that is going to be returned
    new_string = ""
    # Go through all the string
    for char in string:
        if char == last_char:
            count_repet += 1
        else:
            new_string.join([last_char, str(count_repet)])
            count_repet = 1
            last_char = char
    return new_string
