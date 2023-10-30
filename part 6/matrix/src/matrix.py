def reader(matrix: str)-> list :
    list_to_return = []

    with open(matrix) as file_name :
        for line in file_name :
            numbers = []
            line = line.replace("\n", "")
            nums = line.split(",")
            for n in nums :
                n = int(n)
                numbers.append(n)
            #print(numbers)
            list_to_return.append(numbers)
    return list_to_return



def matrix_sum():
    sum_of_matrix = 0
    mat = reader("matrix.txt")
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            sum_of_matrix = sum_of_matrix + mat[i][j]
    return sum_of_matrix


def matrix_max():
    max = 0
    mat = reader("matrix.txt")
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > max :
                max = mat[i][j]
    
    return max



def row_sums():
    sum_of_rows = []
    mat = reader("matrix.txt")
    for i in range(len(mat)) :
        sum_of_rows.append(sum(mat[i]))
    return sum_of_rows




if __name__ == "__main__" :
    summ = matrix_sum()
    #maxx = matrix_max()
    #rowsum = row_sums()
    #print(f"the sum is {summ}, the maximum is {maxx}, and the sum of rows are {rowsum}")



