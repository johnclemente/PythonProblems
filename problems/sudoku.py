# IN PROGRESS

from typing import List
# checking for sudoku validity.

# Approach

# loop through multidemsional array
# for each row, check for no repeat numbers
# for each index, check for no repeat numbers
# box will be tricky...lets think about this later

sudoku_grid = [ 
["5", "3", ".", ".", "7", ".", ".", ".", "."], 
["6", ".", ".", "1", "9", "5", ".", ".", "."], 
[".", "9", "8", ".", ".", ".", ".", "6", "."], 
["8", ".", ".", ".", "6", ".", ".", ".", "3"], 
["4", ".", ".", "8", ".", "3", ".", ".", "1"], 
["7", ".", ".", ".", "2", ".", ".", ".", "6"], 
[".", "6", ".", ".", ".", ".", "2", "8", "."], 
[".", ".", ".", "4", "1", "9", ".", ".", "5"], 
[".", ".", ".", ".", "8", ".", ".", "7", "9"] ]


def isValidSudokuList(sudoku_grid: List[List[str]]) -> bool:
	print(sudoku_grid)    	

isValidSudokuList(sudoku_grid);
