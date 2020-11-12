"""
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
"""

def rotated_array_search(input_list, number,left=0):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    """
    If mid happens to be the point of rotation them both left and right sub-arrays will be sorted
    But in any case one half(sub-array) must be sorted.
    We can easily know which half is sorted by comparing start and end element of each half.
    Once we find which half is sorted we can see if the key is present in that half - simple 
    comparison with the extremes.
    If the key is present in that half we recursively call the function on that half
    else we recursively call our search on the other half.
    """
    if len(input_list) == 0:
        return -1
    start = 0
    end = len(input_list) - 1
    mid = (start+end)//2
    if input_list[mid] == number:
        return mid + left
    # check if left half is sorted
    if input_list[start] <= input_list[mid]:
        # check if target is present in left half
        if input_list[start] <= number <= input_list[mid]:
            return rotated_array_search(input_list[:mid], number,left)
        else:
            # if not available in left half then search in right half
            return rotated_array_search(input_list[mid+1:], number,mid+left+1)
    # if left half is NOT sorted then right half is sorted
    else:
        # check if target is present in right half
        if input_list[mid + 1] <= number <= input_list[end]:
            # print('yes, i m searching in right half')
            return rotated_array_search(input_list[mid+1:], number, mid+left+1)
        else:
            # if not available in right half then search in left half
            return rotated_array_search(input_list[:mid], number, left)
    pass


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# 0
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# 5
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# 2
test_function([[], 0])
test_function([[0], 0])