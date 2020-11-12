def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    You can assume that all array elements are in the range [0, 9]
    The number of digits in both the numbers cannot differ by more than 1
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) <= 1:
        return input_list
    quick_sort_program(input_list)
    something = True
    result = [''] * 2
    for i in range(len(input_list)-1, -1, -1):
        # print (i)
        if something:
            # print(result[0])
            result[0] = int(str(result[0]) + str(input_list[i]))
            something = False
        else:
            result[1] = int(str(result[1]) + str(input_list[i]))
            something = True
    # print result
    return result


def quick_sort_program(array):
    sort_all(array, 0, len(array) - 1)


def sortForPivotIndex(array, begin_index, end_index):
    left_index = begin_index
    pivot_index = end_index
    pivot_value = array[pivot_index]

    while pivot_index != left_index:
        left_value = array[left_index]

        if left_value <= pivot_value:
            left_index += 1
            continue
        else:
            array[left_index] = array[pivot_index - 1]
            array[pivot_index - 1] = pivot_value
            array[pivot_index] = left_value
            pivot_index -= 1
    return pivot_index


def sort_all(array, begin_index, end_index):
    if end_index <= begin_index:
        return
    pivot_index = sortForPivotIndex(array, begin_index, end_index)
    sort_all(array, begin_index, pivot_index-1)
    sort_all(array, pivot_index + 1, end_index)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
# [542, 31]
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# [964, 852]
test_function([[4, 6, 2, 5, 9, 8, 1], [9641, 852]])
# [9641, 852]
test_function([[4], [4]])
# [9641, 852]
test_function([[], []])
# [9641, 852]
