"""
Tic Tac Toe Player
"""

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
    x = 0
    o = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is X:
                x = x + 1
            elif board[i][j] is O:
                o = o + 1

    if x == 0 or o == x:
        print("Players X's turn")
        return X
    else:
        print("Players O's turn")
        return O


def actions(board):
    possible_actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    mango = [row[:] for row in board]
    mango[action[0]][action[1]] = player(board)
    return mango


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        cell = []
        for j in range(len(board[i])):
            cell.append(board[i][j])
        if board[i][0] == board[i][1] == board[i][2] == X:
            return X
        elif board[i][0] == board[i][1] == board[i][2] == O:
            return O
        elif board[0][i] == board[1][i] == board[2][i] == X:
            return X
        elif board[0][i] == board[1][i] == board[2][i] == O:
            return O
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O:
        return O
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    track = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is EMPTY:
                track = False
                break

    if track is True:
        return True

    res = winner(board)
    if res is X or res is O:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    terminal_result = terminal(board)
    if terminal_result is True:
        win = winner(board)
        if win is X:
            return 1
        elif win is O:
            return -1
        else:
            return 0
    else:
        return 0


def minimax(board):
    current_player = player(board)

    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -2
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = 2
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    if current_player is X:
        best_score = -2
        best_action = None
        for action in actions(board):
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_action = action
        return best_action
    else:
        best_score = 2
        best_action = None
        for action in actions(board):
            score = max_value(result(board, action))
            if score < best_score:
                best_score = score
                best_action = action
        return best_action
