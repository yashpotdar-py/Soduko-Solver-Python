#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <algorithm>

class SudokuGenerator {
public:
    SudokuGenerator(std::vector<std::vector<int>> board) : board(board) {}

    bool addValues() {
        std::pair<int, int> empty = findEmpty();
        if (empty.first == -1) {
            return true;  // All cells are filled
        }

        int row = empty.first;
        int col = empty.second;
        std::vector<int> values = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        std::random_shuffle(values.begin(), values.end());

        for (int value : values) {
            if (isValidSquare(row, col, value)) {
                board[row][col] = value;

                if (addValues()) {
                    return true;
                }

                board[row][col] = 0;  // Backtrack if the current configuration doesn't lead to a solution
            }
        }

        return false;
    }

    void printBoard() {
        addValues();
        for (int i = 0; i < 9; i++) {
            if (i % 3 == 0 && i != 0) {
                std::cout << "- - - - - - - - - - - - " << std::endl;
            }
            for (int j = 0; j < 9; j++) {
                if (j % 3 == 0 && j != 0) {
                    std::cout << " | ";
                }
                if (j == 8) {
                    std::cout << board[i][j] << std::endl;
                } else {
                    std::cout << board[i][j] << " ";
                }
            }
        }
    }

private:
    std::vector<std::vector<int>> board;

    std::pair<int, int> findEmpty() {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == 0) {
                    return std::make_pair(i, j);
                }
            }
        }
        return std::make_pair(-1, -1);
    }

    bool isValidSquare(int row, int col, int num) {
        for (int i = 0; i < 9; i++) {
            if (board[row][i] == num || board[i][col] == num) {
                return false;
            }
        }

        int boxRow = (row / 3) * 3;
        int boxCol = (col / 3) * 3;
        for (int i = boxRow; i < boxRow + 3; i++) {
            for (int j = boxCol; j < boxCol + 3; j++) {
                if (board[i][j] == num) {
                    return false;
                }
            }
        }

        return true;
    }
};

class SudokuSolver {
public:
    SudokuSolver(std::vector<std::vector<int>> board) : board(board) {}

    bool solve() {
        std::pair<int, int> empty = findEmpty();
        if (empty.first == -1) {
            return true;  // All cells are filled, Sudoku is solved
        }

        int row = empty.first;
        int col = empty.second;

        for (int num = 1; num <= 9; num++) {
            if (isValid(num, row, col)) {
                board[row][col] = num;

                if (solve()) {
                    return true;  // Continue solving
                }

                board[row][col] = 0;  // Backtrack if the current configuration doesn't lead to a solution
            }
        }

        return false;
    }

    void printBoard() {
        for (int i = 0; i < 9; i++) {
            if (i % 3 == 0 && i != 0) {
                std::cout << "- - - - - - - - - - - - " << std::endl;
            }
            for (int j = 0; j < 9; j++) {
                if (j % 3 == 0 && j != 0) {
                    std::cout << " | ";
                }
                if (j == 8) {
                    std::cout << board[i][j] << std::endl;
                } else {
                    std::cout << board[i][j] << " ";
                }
            }
        }
    }

private:
    std::vector<std::vector<int>> board;

    std::pair<int, int> findEmpty() {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == 0) {
                    return std::make_pair(i, j);
                }
            }
        }
        return std::make_pair(-1, -1);
    }

    bool isValid(int num, int row, int col) {
        for (int i = 0; i < 9; i++) {
            if (board[row][i] == num || board[i][col] == num) {
                return false;
            }
        }

        int boxRow = (row / 3) * 3;
        int boxCol = (col / 3) * 3;
        for (int i = boxRow; i < boxRow + 3; i++) {
            for (int j = boxCol; j < boxCol + 3; j++) {
                if (board[i][j] == num) {
                    return false;
                }
            }
        }

        return true;
    }
};

int main() {
    std::vector<std::vector<int>> sudokuBoard(9, std::vector<int>(9, 0));

    SudokuGenerator sudokuGenerator(sudokuBoard);
    std::cout << "Original Sudoku Board:" << std::endl;
    sudokuGenerator.printBoard();
    std::cout << "#############################" << std::endl;

    SudokuSolver sudokuSolver(sudokuBoard);
    if (sudokuSolver.solve()) {
        std::cout << "Solved Sudoku:" << std::endl;
        sudokuSolver.printBoard();
    } else {
        std::cout << "No solution exists." << std::endl;
    }

    return 0;
}
