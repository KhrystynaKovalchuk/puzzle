"""
Task2
"""

def check_uniqueness(digits: list) -> bool:
    """
    Checks if elements in the lists are different.
    >>> check_uniqueness([1, 2, 3])
    True
    >>> check_uniqueness([2, 4, 4])
    False
    """
    unique = set(digits)
    if len(unique) == len(digits):
        return True
    return False


def horizontal_check(board: list) -> bool:
    """
    Checks if there aren't the same digits in the rows.
    >>> horizontal_check([])
    True
    """
    digits = []
    correct = []
    for line in board:
        for i in range(len(line)):
            if line[i] != "*" and line[i] != " ":
                digits.append(int(line[i]))
        if check_uniqueness(digits) == True:
            digits.clear()
            continue
        else:
            correct.append(False)
        digits.clear()
    if correct == []:
        return True
    return False


def form_columns(board: list) -> list:
    """
    Returns columns of the board.
    >>> form_columns([])
    ['', '', '', '', '', '', '', '', '']
    """
    lst = []
    general = []
    for i in range(9):
        for line in board:
            lst.append(line[i])
        general.append("".join(lst))
        lst.clear()
    return general


def check_columns(board: list) -> bool:
    """
    Checks columns on different digits.
    >>> check_columns([])
    True
    """
    columns = form_columns(board)
    return horizontal_check(columns)


def check_blocks(board: list) -> bool:
    """
    Checks certain blocks on different digits.
    >>> check_blocks([\
     "**** ****",\
     "***1 ****",\
     "**  3****",\
     "* 4 1****",\
     "     9 5 ",\
     " 6  83  *",\
     "3   1  **",\
     "  8  2***",\
     "  2  ****"\
    ])
    True
    """
    columns = form_columns(board)
    line_block = []
    columns_block = []
    line_block.append(board[1][-1])
    columns_block.append(columns[0])
    for i in range(1, 10):
        try:
            line_block.append(board[i][8-i: 10])
            columns_block.append(columns[i][0:9-i])
        except IndexError:
            continue
    meanings = []
    for elem in range(len(line_block)-1):
        checking_line = line_block[elem][1:] + columns_block[::-1][elem]
        meanings.append(checking_line)
    return horizontal_check(meanings)


def validate_board(board):
    """
    Defines if board is ready for a game by 3 characteristics.
    >>> validate_board([\
     "**** ****",\
     "***1 ****",\
     "**  3****",\
     "* 4 1****",\
     "     9 5 ",\
     " 6  83  *",\
     "3   1  **",\
     "  8  2***",\
     "  2  ****"\
    ])
    False
    """
    line = horizontal_check(board)
    column = check_columns(board)
    block = check_blocks(board)
    if line == True and column == True and block == True:
        return True
    return False
