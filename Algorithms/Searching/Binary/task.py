def binary_search(arr: list, item: int) -> int:
    l_index = 0
    r_index = len(arr) - 1

    if item < arr[l_index] or item > arr[r_index]:
        return -1

    while l_index <= r_index:
        middle_index = (l_index + r_index) // 2

        if arr[middle_index] == item:
            return middle_index
        elif arr[middle_index] < item:
            l_index = middle_index + 1
        elif arr[middle_index] > item:
            r_index = middle_index - 1

    return -1


# Binary search works with only sorted elements
result = binary_search([1, 3, 4, 6, 7, 8, 10, 12, 23, 45, 56, 78, 99], 23)
print(result)
