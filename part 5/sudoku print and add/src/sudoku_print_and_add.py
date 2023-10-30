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
        



def add_number(sudoku: list, row: int, column: int, number: int):
    sudoku[row][column] = number





if __name__ == "__main__" :
    sudoku  = [
    [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
    [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
    [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
    [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
    [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
    [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
    [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
    [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
    ]

    print_sudoku(sudoku)
            