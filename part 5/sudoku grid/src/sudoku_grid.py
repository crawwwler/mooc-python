def sudoku_grid_correct(sudoku: list):
    err = 0
    x = 0
    if err == 0 :
        for i in range(0, 9):
            if row_correct(sudoku, i) == False :
                err += 1
                break

    
    if err == 0 :
        for i in range(0, 9):
            if column_correct(sudoku, i) == False:
                err += 1
                breaK

    if err == 0 :
        for i in [0,3,6]:
            if block_correct(sudoku, x, i) == False:
                err += 1
                break
            else :
                x += 3

    
    return err == 0




def block_correct(sudoku: list, row: int, col: int):
    checker = []
    err =  True
    for n in range(3):
        helper = sudoku[row][col:col+3]
        for i in helper :
            if not(i in checker):
                if i != 0 :
                    checker.append(i)
                else :
                    continue
            else :
                err = False
        row += 1
    return err



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




if __name__ == "__main__":

    sudoku = [
    [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [ 0, 5, 1, 6, 0, 0, 8, 3, 9 ],
    [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]

    

    sudoku_grid_correct(sudoku) #CALLING THE A FUNCTION