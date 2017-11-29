def sum_iter(array):
    sum = 0
    for el in array:
        sum += el
    return sum


def sum_rec(array):
    if not array:
        return 0
    return array[0] + sum_rec(array[1:])


list = [1, 4, 5, 9]
print sum_iter(list)
print sum_rec(list)