def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):

    nulist = sudoku[:]
    # as every index of an matrix, is a list, we should create new list 
    # and put them into the nulist, otherwise indexes of nulist just refer to
    # indexes of sudoku list ( the main list that we should not modify)
    for i in range(len(nulist)):
        neww = []
        neww = sudoku[i][:]
        nulist[i] = neww
    
    nulist[row_no][column_no] = number
    return nulist



def print_sudoku(sudoku: list):
    
    y = 0
    for i in range(len(sudoku)):
        x = 0
        if y != 0 and y %3 ==0:
            print()
        for j in range(len(sudoku[i])):
            if x != 0 and x % 3 == 0:
                print(" ", end="")
            if sudoku[i][j] == 0 :
                print("_", end=" ")
            else :
                print(f"{sudoku[i][j]}", end=" ")
            x += 1
        y += 1
        print()


if __name__ == "__main__":
    s = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 5, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    ]

    print_sudoku(s)
    print()
    res = copy_and_add(s,1,1,3)
    print_sudoku(s)
    print()
    print_sudoku(res)