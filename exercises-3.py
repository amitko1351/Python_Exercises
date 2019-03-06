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


def check_row(matrix):
    """
    The function check if someone won base on the row 
    :param matrix: the game board
    :return: return 1 if the first player won
             return 2 if the second player won
             else if nobody won return 0
    """
    # Go over all the rows and search for winner
    for row in matrix:
        potential_winner = row[0]
        is_won = all(potential_winner == block for block in row)
        if is_won:
            return potential_winner
    return 0


def check_col(matrix):
    """
       The function check if someone won base on the col 
       :param matrix: the game board
       :return: return 1 if the first player won
             return 2 if the second player won
             else if nobody won return 0
    """
    # Go over all the cols and search for winner
    for col_number in range(3):
        potential_winner = matrix[0][col_number]
        is_won = all(potential_winner == row[col_number] for row in matrix)
        if is_won:
            return potential_winner
    return 0


def check_diagonal(matrix):
    """
    The function check if someone won base on the diagonal 
    :param matrix: the game board
    :return: return 1 if the first player won
             return 2 if the second player won
             else if nobody won return 0
    """
    # Check the main diagonal
    is_won = all(matrix[0][0] == matrix[i][i] for i in range(3))
    if is_won:
        return matrix[0][0]
    # Check the main diagonal
    is_won = all(matrix[2][0] == matrix[2-i][i] for i in range(3))
    if is_won:
        return matrix[2][0]
    return 0

def check_win(matrix):
    """
    the function check if one of the players won
    :param matrix: the game board
    :return: return 1 if the first player won
             return 2 if the second player won
             else if nobody won return 0
    """
    # The player who won
    win_player = 0
    win = check_row(matrix)
    if win:
        return win
    win = check_col(matrix)
    if win:
        return win
    return check_diagonal(matrix)
