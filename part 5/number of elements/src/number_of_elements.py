def count_matching_elements(my_matrix: list, num: int):
    count = 0 
    for i in range(len(my_matrix)):
        for j in range(len(my_matrix[i])):
            if my_matrix[i][j] == num :
                count += 1
    return count