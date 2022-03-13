import sudoku

#If you would like to play and need a board, there is an image uploaded which is titled Board4.png 

##Asking for input
print("Welcome to Sudoku Solver. This works best for easy and medium puzzles.\n")
row1 = input("Please enter all the values of the first (top) row. For a blank, enter a space.\n")
row2 = input("Please enter all the values of the second (from top) row. For a blank, enter a space.\n")
row3 = input("Please enter all the values of the third (from top) row. For a blank, enter a space.\n")
row4 = input("Please enter all the values of the fourth (from top) row. For a blank, enter a space.\n")
row5 = input("Please enter all the values of the fifth (from top) row. For a blank, enter a space.\n")
row6 = input("Please enter all the values of the sixth (from top) row. For a blank, enter a space.\n")
row7 = input("Please enter all the values of the seventh (from top) row. For a blank, enter a space.\n")
row8 = input("Please enter all the values of the eighth (from top) row. For a blank, enter a space.\n")
row9 = input("Please enter all the values of the ninth (from top) row. For a blank, enter a space.\n")

sudoku_string = row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8 + row9

board5 = sudoku.Board(sudoku_string)
board5.make_solve_print()



# board1 = sudoku.Board("  88 947  2  6   1 7     694     1    21 88 63  94  8823 75 6945    38  69   235 ")

# board1.make_board()

# print(board1.print_board())

# print(board1.check_board())

# board2 = sudoku.Board("2648 3      6  52 9  7 1 46 139       94 68       293 87 3 9  1 41  5      1 7284")

# board2.make_solve_print()

# board3 = sudoku.Board("9 7  6  4    7 3 94   8 167  3  7  179  5  321  2  5  825 9   36 9 1    3  5  7 8")

# board3.make_solve_print()

# board3 = sudoku.Board("6    2 9  9     381 354  6 9  2   7 8 61 49 3 2   7  4 6  137 223     4  4 6    9")

# board3.make_solve_print()

##A picture of Board4 is in the files
# board4 = sudoku.Board("9 1  5 3  4  62  7  63 142  1493   8         6   2719  382 46  1  68  4  6 7  2 1")

# ##Board solved
# board4.make_solve_print()