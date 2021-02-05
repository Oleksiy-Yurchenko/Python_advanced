# 1) Write a function def solution(A) that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.


def smallest_integer(input_array):
    if not input_array:
        return "Please input a non-empty list as a function's argument."
    arr_max = max(input_array)
    Z_plus  = set(range(1,arr_max + 1)) # Set of all positive integers from 1 to max(arr)
    set_input_array = set(input_array)
    set_positive = set_input_array.intersection(Z_plus) # Set of positive integers of the input array
    if arr_max < 1:
        return 1
    try:
        min_int = min(Z_plus.difference(set_positive))
    except ValueError:
        return arr_max + 1
    return min_int

print('Smallest integer([-1,-3]) =', smallest_integer([-1,-3]))
print('Smallest integer([0]) =', smallest_integer([0]))
print('Smallest integer([]) =', smallest_integer([]))
print('Smallest integer((1,2,3)) =', smallest_integer((1,2,3)))
print('Smallest integer([-1, 0, 3, 12, 36]) =', smallest_integer([-1, 0, 3, 12, 36]))
print('Smallest integer([-1, 0, 0, 1, 1, 3, 12, 36]) =', smallest_integer([-1, 0, 0, 1, 1, 3, 12, 36]))


# 2)A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.
# Write a function:
# def solution(N)
# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.


def binary_parser(input_number):
    input_number_str = '{0:b}'.format(input_number)
    gap_Flag = False
    max_gap = 0
    current_gap = 0
    for c in input_number_str:
        if int(c) and not gap_Flag:
            gap_Flag = True
        elif not int(c) and gap_Flag:
            current_gap += 1
        elif gap_Flag and int(c):
            if current_gap > max_gap:
                max_gap = current_gap
                current_gap = 0
    return max_gap

print('Max Gap 9 = ', binary_parser(9))
print('Max Gap 529 = ', binary_parser(529))
print('Max Gap 20 = ', binary_parser(20))
print('Max Gap 15 = ', binary_parser(15))
print('Max Gap 1041 = ', binary_parser(15))
print('Max Gap 32 = ', binary_parser(32))


# 3)An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).
# The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.
# Write a function:
# def solution(A, K)
# that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.
# For example, given
#     A = [3, 8, 9, 7, 6]
#     K = 3
# the function should return [9, 7, 6, 3, 8]. Three rotations were made:
#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
# For another example, given
#     A = [0, 0, 0]
#     K = 1
# the function should return [0, 0, 0]
# Given
#     A = [1, 2, 3, 4]
#     K = 4
# the function should return [1, 2, 3, 4]


def array_shift(array, shift):
    arr_from_range = range(len(array))
    return [array[i - shift] if shift > 0 else array[i + shift] for i in arr_from_range]

print('array_shift([3,8,9,7,6], 3) = ', array_shift([3,8,9,7,6], 3))
print('array_shift([0,0,0], 3) = ', array_shift([0,0,0], 3))
print('array_shift([1,2,3,4], 4) = ', array_shift([1,2,3,4], 4))
print('array_shift([], 3) = ', array_shift([], 3))
print('array_shift([3,8,9,7,6], 3) = ', array_shift([3,8,9,7,6], -3))
