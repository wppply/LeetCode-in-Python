def reverse_merge_sort(str_arr):
    """
    abcd1234 to a1b2c3d4
    a1 b2 c3 d4
    ab 12 cd 34
    ab cd 12 34

    """
    # ending criteria
    if len(str_arr) < 4:
        return

    idx_14 = len(str_arr) // 4
    idx_24 = len(str_arr) // 4 * 2
    idx_34 = len(str_arr) // 4 * 3
    str_arr[idx_14: idx_34] = str_arr[idx_14: idx_34][::-1]
    str_arr[idx_14: idx_24] = str_arr[idx_14: idx_24][::-1]
    str_arr[idx_24: idx_34] = str_arr[idx_24: idx_34][::-1]
    return


def reverse_string(str_arr):
    return str_arr[::-1]

