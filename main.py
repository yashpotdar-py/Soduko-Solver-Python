import random


class SudokuGenerator:

    def __init__(self, board):
        """
        Initialize a SudokuSolver object with a 9x9 Sudoku board.

        Args:
            board (list): A 9x9 Sudoku board represented as a list of lists.
                          Empty cells are represented by 0.
        """
        self.board = board

    def find_empty(self):
        """
        Find the first empty cell in the Sudoku board.

        Returns:
            tuple or None: A tuple (row, col) representing the empty cell, or None if no empty cell exists.
        """

        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def valid_square(self, row, col, num):
        """
        Check is the value in the square is valid

        Args:
            num (int): The number to be checked.
            row (int): Row index of the cell.
            col (int): Column index of the cell.
        """

        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.board[i][j] == num:
                    return False
        return True

    def add_values(self):
        empty = self.find_empty()
        if not empty:
            return True  # all cells are filled

        row, col = empty
        # generate a list with random values e.g. [7,5,3,1,4,2,9,8,6]
        values = random.sample(range(1, 10), 9)

        for value in values:
            if self.valid_square(row, col, value):
                self.board[row][col] = value

                if self.add_values():
                    return True

        return False

    def print_board(self):
        """
        Print the current state of the Sudoku board in a human-readable format.
        """
        self.add_values()
        self.remove_random_values()
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(self.board[i][j], end=" ")

    def remove_random_values(self):
        """
        Remove a specified number of random values from the Sudoku board and set them to zero.
        """
        num_to_remove = random.randint(0, 81)
        if num_to_remove < 0 or num_to_remove > 81:
            raise ValueError(
                "Number of values to remove must be between 0 and 81.")

        cells = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(cells)

        for _ in range(num_to_remove):
            i, j = cells.pop()
            self.board[i][j] = 0


class SudokuSolver:
    def __init__(self, board):
        """
        Initialize a SudokuSolver object with a 9x9 Sudoku board.

        Args:
            board (list): A 9x9 Sudoku board represented as a list of lists.
                          Empty cells are represented by 0.
        """
        self.board = board

    def is_valid(self, num, row, col):
        """
        Check if it's valid to place a number in a specific cell.

        Args:
            num (int): The number to be placed.
            row (int): Row index of the cell.
            col (int): Column index of the cell.

        Returns:
            bool: True if it's valid to place the number, False otherwise.
        """
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.board[i][j] == num:
                    return False
        return True

    def solve(self):
        """
        Solve the Sudoku puzzle using backtracking.

        Returns:
            bool: True if a solution is found, False if no solution exists.
        """
        empty = self.find_empty()
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.is_valid(num, row, col):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0

        return False

    def find_empty(self):
        """
        Find the first empty cell in the Sudoku board.

        Returns:
            tuple or None: A tuple (row, col) representing the empty cell, or None if no empty cell exists.
        """
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def print_board(self):
        """
        Print the current state of the Sudoku board in a human-readable format.
        """
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(self.board[i][j], end=" ")


if __name__ == "__main__":
    sudoku_board = [[0 for _ in range(9)] for _ in range(9)]

    sudoku_generator = SudokuGenerator(sudoku_board)
    sudoku_generator.print_board()

    sudoku_solver = SudokuSolver(sudoku_board)
    print("Original Sudoku Board:")
    sudoku_solver.print_board()
    print("#############################")

    if sudoku_solver.solve():
        print("Solved Sudoku:")
        sudoku_solver.print_board()
    else:
        print("No solution exists.")
