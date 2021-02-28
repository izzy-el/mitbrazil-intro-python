def run_length_encode_2d(array):
    compact_list = []
    equal_numbers_counter = 0
    current_number = array[0][0]

    for current_loop, cells in enumerate(array):
        for row in cells:
            if row == current_number:
                equal_numbers_counter += 1
            elif row != current_number or current_loop == len(cells) - 1:
                compact_list.append((equal_numbers_counter, current_number))
                current_number = row
                equal_numbers_counter = 1

    compact_list.append((equal_numbers_counter, current_number))
    
    return compact_list
            

# run_length_encode_2d([  [1, 1, 1, 1, 1, 1, 1],
#                         [1, 0, 0, 0, 0, 0, 1],
#                         [1, 0, 1, 0, 1, 0, 1],
#                         [1, 0, 0, 0, 0, 0, 1],
#                         [1, 0, 1, 1, 1, 0, 1],
#                         [1, 0, 0, 0, 0, 0, 1],
#                         [1, 1, 1, 1, 1, 1, 1]])

