def row_sums(my_matrix: list):

    for i in range(len(my_matrix)):
        sum_of_row = 0
        for j in my_matrix[i]:
            sum_of_row += j
        my_matrix[i].append(sum_of_row)
        