def binary_search_iter(list, item):
    start = 0
    end = len(list) - 1
    while start <= end:
        middle = (end + start) / 2
        if list[middle] == item:
            return middle
        if list[middle] < item:
            start = middle + 1
        else:
            end = middle - 1
    return None


l = [1, 5, 7, 9, 10, 22]
print binary_search_iter(l, 10)
