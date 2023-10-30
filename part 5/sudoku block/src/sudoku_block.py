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