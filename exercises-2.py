def sum_input_numbers():
    """
    the function gets from the user the number to sum up
    """
    # The number the program gets
    number = input("Please enter the number (enter stop for result)")
    # The sum of the numbers
    sum_of_numbers = 0
    while True:
        if number == "stop":
            print("the sum is {}".format(str(sum_of_numbers)))
            break
        if number.isdigit():
            sum_of_numbers += int(number)
        number = input("Please enter the number (enter stop for result)")
