def binarySearch(arr: list, item: int) -> int:
    L = 0
    R = len(arr) - 1
    while L <= R:
        m = (L + R) // 2
        if arr[m] == item:
            return m
        elif arr[m] < item:
            L = m + 1
        elif arr[m] > item:
            R = m - 1
    return None

result = binarySearch([1,3,4,6,7,8,10,12,23,45,56,78,99], 23)
print(result)
