def column_correct(sudoku: list, column_no: int):
    checker = []
    error = True 
    for i in range(len(sudoku)) :
        if not(sudoku[i][column_no] in checker):
            if sudoku[i][column_no] != 0 :
                checker.append(sudoku[i][column_no])
            else :
                continue
        else :
            error = False
    return error

