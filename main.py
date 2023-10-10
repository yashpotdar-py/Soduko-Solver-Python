def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(f"{board[i][j]}")
            else:
                print(f"{board[i][j]} ", end="")


def valid_board(board, num, pos):
    row, col = pos

    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check box
    box_row = row // 3
    box_col = col // 3
    for i in range(box_row * 3, (box_row + 1) * 3):
        for j in range(box_col * 3, (box_col + 1) * 3):
            if board[i][j] == num:
                return False

    return True


def solve_board(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if valid_board(board, num, (row, col)):
            board[row][col] = num
            if solve_board(board):
                return True
            board[row][col] = 0

    return False


def find_empty(board):
    for row, row_vals in enumerate(board):
        for col, val in enumerate(row_vals):
            if val == 0:
                return row, col
    return None


if __name__ == "__main__":
    sudoku_board = [
        # 9x9 Sudoku board
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print_board(sudoku_board)
    print("#############################")
    if solve_board(sudoku_board):
        print_board(sudoku_board)
    else:
        print("No solution exists.")
