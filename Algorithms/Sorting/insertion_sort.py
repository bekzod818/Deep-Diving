def insertion_sort(array: list) -> list:
    for index in range(1, len(array)):
        current_element = array[index]
        previous_index = index - 1
        while previous_index >= 0 and array[previous_index] > current_element:
            array[previous_index + 1] = array[previous_index]
            print(array[previous_index + 1], previous_index)
            previous_index -= 1
        array[previous_index + 1] = current_element
    return array


result = insertion_sort([4, 2, 0, 9, 5, 6, 1, 7, 3, 8])
print(result)

# 1-step # [2, 4, 0, 9, 5, 6, 1, 7, 3, 8]
# 2-step # [0, 2, 4, 9, 5, 6, 1, 7, 3, 8]
# 3-step # [0, 2, 4, 9, 5, 6, 1, 7, 3, 8]
# 4-step # [0, 2, 4, 5, 9, 6, 1, 7, 3, 8]
# 5-step # [0, 2, 4, 5, 6, 9, 1, 7, 3, 8]
# 6-step # [0, 1, 2, 4, 5, 6, 9, 7, 3, 8]
# 7-step # [0, 1, 2, 4, 5, 6, 7, 9, 3, 8]
# 8-step # [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
# 9-step # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
