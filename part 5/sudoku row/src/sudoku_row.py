def row_correct(sudoku: list, row_no: int):
    checker = []
    errors = True
    for j in range(len(sudoku[row_no])):
        if not(sudoku[row_no][j] in checker):
            if sudoku[row_no][j] != 0 :
                checker.append(sudoku[row_no][j])
            else :
                continue
        else :
            errors = False
    
    return errors 

        



if __name__ == "__main__" :
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))