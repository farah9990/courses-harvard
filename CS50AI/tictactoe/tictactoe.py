"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numX = 0
    numO = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != EMPTY:
                if board[i][j] == X:
                    numX += 1
                else:
                    numO += 1

    if numX > numO:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    position = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                position.add((i, j))
    return position


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action in actions(board):
        i, j = action
        cboard = copy.deepcopy(board)
        cboard[i][j] = player(board)
        return cboard
    else:
        raise Exception("NOT valid ")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(len(board)):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        if board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O
    for j in range(len(board)):
        if board[0][j] == X and board[1][j] == X and board[2][j] == X:
            return X
        if board[0][j] == O and board[1][j] == O and board[2][j] == O:
            return O
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[2][2] == X and board[1][1] == X and board[0][0] == X:
        return X
    if board[2][2] == O and board[1][1] == O and board[0][0] == O:
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def maxt(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, mint(result(board, action)))
    return v


def mint(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = min(v, maxt(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        p = []
        for action in actions(board):
            p.append([mint(result(board, action)), action])
        return sorted(p, key=lambda x: x[0], reverse=True)[0][1]
    if player(board) == O:
        p = []
        for action in actions(board):
            p.append([maxt(result(board, action)), action])
        return sorted(p, key=lambda x: x[0])[0][1]