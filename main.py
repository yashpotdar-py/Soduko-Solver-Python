from generator import SudokuGenerator
from solver import SudokuSolver

sudoku_board = [[0 for _ in range(9)] for _ in range(9)]

sudoku_generator = SudokuGenerator(sudoku_board)

print("Original Sudoku Board:")
sudoku_generator.print_board()
print("#############################")

sudoku_solver = SudokuSolver(sudoku_board)
print("\nSolved Sudoku:")
sudoku_solver.solve()
sudoku_solver.print_board()