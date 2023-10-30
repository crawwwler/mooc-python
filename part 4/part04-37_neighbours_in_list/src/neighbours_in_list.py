def longest_series_of_neighbours(nums : list)-> int:
    current = []
    longest = []

    for i in range(len(nums)-1) :
        if abs(nums[i] - nums[i+1]) == 1 :
            current.append(nums[i])
        else :
            current.append(nums[i])
            if len(current) > len(longest) :
                longest = current
            current = []
    current. append(nums[-1])
    if len(current) > len(longest) :
        longest = current
    
    return len(longest)




if __name__ == "__main__" :
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))


