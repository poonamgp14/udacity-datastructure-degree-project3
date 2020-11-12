def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if len(input_list) <= 1:
        return input_list
    next_post_0 = 0
    next_post_2 = len(input_list) - 1
    front_index = 0
    while front_index <= next_post_2:
        current_value = input_list[front_index]
        if current_value == 0:
            next_0_value = input_list[next_post_0]
            input_list[next_post_0] = 0
            input_list[front_index] = next_0_value
            next_post_0 += 1
            front_index += 1
        elif current_value == 2:
            next_2_value = input_list[next_post_2]
            input_list[next_post_2] = 2
            input_list[front_index] = next_2_value
            next_post_2 -= 1
        else:
            front_index +=1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")
test_function([0, 0, 2, 1, 1, 1, 2, 0, 1])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 1])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
test_function([2])