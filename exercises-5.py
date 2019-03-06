def final_sum(num):
    """
    The function finds the final sum of num
    :param num: the number which is summed
    :return: the final sum of the number
    """
    # The final sum
    fsum = 0
    while True:
        if num < 10:
            return fsum + num
        fsum = num % 10
        num = num / 10


def sum_digits(digits_to_sum):
    """
    The function generate the special sum of the digits
    :param digits_to_sum: the digit it need to sum
    :return: return the special sum
    """
    # The place of the digit
    place = 1
    # Sum of digits
    sum_of_digits = 0
    # Go through all the digits
    for digit in digits_to_sum:
        if place % 2 == 1:
            sum_of_digits += int(digit)
        else:
            sum_of_digits += final_sum(int(digit)*2)
        place += 1
    return  sum_of_digits


def find_closest_product_to_ten(number):
    """
    The function finds the closest product to ten
    :param number: the number which the function work on
    :return: the closest product to ten 
    """
    return (number / 10 + 1) * 10


def check_id(id):
    """
    the function check the validation of the if
    :param id: id to check (string)
    :return: return true if is valid else false
    """
    # The check digit
    check_digit = id[len(id)-1]
    # The digits need to be sum
    digits_to_sum = id[:len(id)-1]
    sum_of_digits = sum_digits(digits_to_sum)
    product_ten = find_closest_product_to_ten(sum_of_digits)
    return int(check_digit) == (product_ten - sum_of_digits)
