def sum_input_numbers():
    """
    the function gets from the user the number to sum up
    """
    # The number the program gets
    number = input("Please enter the number (enter stop for result)\n")
    # The sum of the numbers
    sum_of_numbers = 0
    while True:
        if number == "stop":
            print("the sum is {}".format(str(sum_of_numbers)))
            break
        if number.isdigit():
            sum_of_numbers += int(number)
        number = input("Please enter the number (enter stop for result)\n")


def sum_ele_from_list():
    """
    sum the elements of the list that entered by the user
    """
    # Get the list from he user
    list_ele = input("Enter the list of number (like that :'1,2,3')\n")
    # Make a list from the numbers
    list_ele = [int(num) for num in list_ele.split(",")]
    print("the sum is {}".format(str(sum(list_ele))))


def main():
    sum_input_numbers()
    sum_ele_from_list()

if __name__ == "__main__":
    main()
