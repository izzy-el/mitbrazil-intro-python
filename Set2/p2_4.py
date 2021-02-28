import sys

# The lowest number in Python is -2147483647. Therefore,
# I used the 'sys' library to get the lowest possible value
def largest_number(input_list):
    if len(input_list) == 0 or len(input_list) == 1:
        return None
    best_so_far = sys.maxsize * -1
    for i in input_list:
        if i > best_so_far:
            best_so_far = i
    return best_so_far

def second_largest_number(input_list):
    if len(input_list) == 0 or len(input_list) == 1:
        return None
    else:
        input_list.remove(largest_number(input_list))
        return largest_number(input_list)
