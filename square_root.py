def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    The expected time complexity is O(log(n))
    """
    if number == 0 or number == 1:
        return number
    if number < 0:
        print 'Needs a positive integer'
        return None
    start = 1
    end = number
    # ans = 0
    while start <= end:
        mid = (start + end) // 2
        result = mid*mid
        if result == number:
            return mid
        elif result > number:
            end = mid - 1
        else:
            # since we need floor value,
            # we update answer when result is less
            # than number
            start = mid + 1
            ans = mid

    return ans

print ("Pass" if (3 == sqrt(9)) else "Fail")
# Pass
print ("Pass" if (0 == sqrt(0)) else "Fail")
# pass
print ("Pass" if (4 == sqrt(16)) else "Fail")
# pass
print ("Pass" if (1 == sqrt(1)) else "Fail")
print ("Pass" if (5 == sqrt(27)) else "Fail")
print ("Pass" if (None is sqrt(-27)) else "Fail")