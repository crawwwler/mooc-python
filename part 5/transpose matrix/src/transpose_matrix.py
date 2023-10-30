def transpose(matrix: list): 

    newDesign = []
    for j in range(len(matrix)):
        helper = []
        for i in range(len(matrix)):
            helper.append(matrix[i][j])
        newDesign.append(helper)
    matrix[:] = newDesign




if __name__ == "__main__" :
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(transpose([[1,2],[1,2]]))
