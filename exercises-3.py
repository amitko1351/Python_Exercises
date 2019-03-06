def input_game_board():
    """
    the function gets from the user the game board
    :return: the game board
    """
    matrix = []
    for i in range(3):
        list = []
        for j in range(3):
            num = input("enter the [{}][{}] ele\n".format(i,j))
            list.append(num)
        matrix.append(list)
    return matrix
