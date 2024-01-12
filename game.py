import random

# Constants representing players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != EMPTY for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def evaluate(board):
    if is_winner(board, PLAYER_X):
        return 1
    elif is_winner(board, PLAYER_O):
        return -1
    else:
        return 0

def minimax(board, depth, maximizing_player):
    if is_winner(board, PLAYER_X):
        return 1
    elif is_winner(board, PLAYER_O):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = PLAYER_X
            eval = minimax(board, depth + 1, False)
            board[i][j] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = PLAYER_O
            eval = minimax(board, depth + 1, True)
            board[i][j] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = float('-inf')
    best_move = None

    for i, j in get_empty_cells(board):
        board[i][j] = PLAYER_X
        move_val = minimax(board, 0, False)
        board[i][j] = EMPTY

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move

def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]

    while True:
        print_board(board)

        # Player's move
        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] != EMPTY:
            print("Cell already occupied. Try again.")
            continue
        board[row][col] = PLAYER_O

        # Check for a win or a draw
        if is_winner(board, PLAYER_O):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI's move
        print("AI is making a move...")
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = PLAYER_X

        # Check for a win or a draw
        if is_winner(board, PLAYER_X):
            print_board(board)
            print("AI wins! Better luck next time.")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
