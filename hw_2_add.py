def smallest_integer(array):
    if not array:
        return print("Please enter as argument a non-empty list")
    else:
        arr_max = max(array)
        return min(set(array).intersection(set(range(1,arr_max + 1)))) if arr_max > 0 else 1


print(smallest_integer([0]))
print(smallest_integer((1,2,3)))
print(smallest_integer([-1, 0, 3, 12, 36]))
print(smallest_integer([-1, 0, 0, 1, 1, 3, 12, 36]))


def binary_parser(N):
    N_str = '{0:b}'.format(N)
    gap_Flag = False
    max_gap = 0
    gap = 0
    for c in N_str:
        if int(c) and not gap_Flag:
            gap_Flag = True
        elif not int(c) and gap_Flag:
            gap += 1
        elif gap_Flag and int(c):
            if max_gap > gap:
                gap = max_gap
            max_gap = 0
    return max_gap

print(binary_parser(345))
print(binary_parser(100))
            

def array_shift(array, shift):
    arr_from_range = range(len(array))
    return [array[i - shift] if shift > 0 else array[i + shift] for i in arr_from_range]

print(array_shift([3,8,9,7,6], 3))
print(array_shift([0,0,0], 3))
print(array_shift([1,2,3,4], 4))
print(array_shift([], 3))
print(array_shift([3,8,9,7,6], -3))
